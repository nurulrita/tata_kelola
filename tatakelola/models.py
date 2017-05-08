from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


KATEGORI_APLIKASI = (
    ('PP', 'Pelayanan Publik'),
    ('MI', 'Manajemen Internal')
)

MEKANISME_PENGANGGARAN = (
    ('O', 'Pengeluaran Operasi'),
    ('C', 'Pengeluaran Modal')
)

JENIS_USER = (
	('OPD', 'OPD'),
	('KOM', 'Diskominfo')
)

STATUS = (
    ('T', 'Diterima'),
    ('DT', 'Ditolak')
)

LATEST_STEP = (
    ('PS', 'Perencanaan Sistem'),
    ('MB', 'Manajemen Belanja'),
    ('RS', 'Realisasi Sistem'),
    ('OS', 'Pengoperasian Sistem'),
    ('MS', 'Pemeliharaan Sistem')
)

class Proyek(models.Model):
    nama_proyek = models.CharField(max_length = 128)
    latest_step = models.CharField(max_length=32, choices=LATEST_STEP)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    opd = models.ForeignKey(User)
    status = models.CharField(max_length = 9, choices=STATUS)


class Step1(models.Model):
    proyek = models.ForeignKey(Proyek)
    arsitektur_informasi = models.FileField()
    kategori_aplikasi = models.CharField(max_length=32, choices=KATEGORI_APLIKASI)
    infrastruktur_komunkasi = models.FileField()
    infrastruktur_penyimpanan_data = models.FileField()
    organisasi_manajemen_realisasi = models.FileField()
    organisasi_manajemen_operasi = models.FileField()
    organisasi_manajemen_pemeliharaan = models.FileField()
    estimasi_waktu = models.IntegerField(help_text='dalam bulan')

class Step2(models.Model):
    proyek = models.ForeignKey(Proyek)
    mekanisme_penganggaran = models.CharField(max_length=32, choices=MEKANISME_PENGANGGARAN)
    umur_ekonomis = models.IntegerField(help_text='dalam bulan')
    ketersediaan_anggaran = models.FileField()
    tingkat_kecepatan_keusangan = models.TextField()
    nilai_startegis_tik = models.TextField()
    karakteristik_proyek = models.TextField()
    urgensi = models.TextField()
    ketersediaan_pemasok = models.TextField()
    ketersediaan_sumber_daya = models.TextField()
    capital_budgeting = models.TextField()
    visi = models.TextField()
    misi = models.TextField()

class Step3 (models.Model):
    proyek = models.ForeignKey(Proyek)
    identifikasi_pemeliharaan_alternatif_sistem = models.TextField()
    realisasi_software_aplikasi = models.TextField()
    realisasi_inrastruktur_teknologi = models.TextField()
    realisasi_pengelolaan_data = models.TextField()

class Step4 (models.Model):
    proyek = models.ForeignKey(Proyek)
    manajemen_tingkat_layanan = models.TextField()
    keamanan_keberlangsungan_sistem = models.TextField()
    manajemen_software_aplikasi = models.TextField()
    manajemen_infratruktur = models.TextField()
    manajemen_data = models.TextField()
    manajemen_pihak_ketiga = models.TextField()

class Step5 (models.Model):
    proyek = models.ForeignKey(Proyek)
    pemeliharaan_software_aplikasi = models.TextField()
    pemeliharaan_infrastruktur_teknologi = models.TextField()
    pemeliharaan_data = models.TextField()
    siklus_hidup_likuidasi_sdit = models.TextField()

class Kebijakan(models.Model):
	nama_perwal = models.CharField(max_length=128)
	no_perwal = models.CharField(max_length=128)
	proyek = models.ForeignKey(Proyek, null=True)
	risiko_proyek = models.TextField()
	risiko_informasi = models.TextField()
	risiko_keberlangsungan_layanan = models.TextField()
	implementasi_project_governance = models.TextField()
	implementasi_security_goernance = models.TextField()
	sumber_dana = models.TextField()
	penganggaran_modal = models.TextField()
	prosedur_pengadaan = models.TextField()
	prioritas_anggaran = models.TextField()
	perhitungan_manfaat_biaya = models.TextField()
	efisiensi_finansial = models.TextField()
	file = models.FileField()

class EvaluasidanMonitor(models.Model):
	opd = models.ForeignKey(User)
	proyek = models.ForeignKey(Proyek, null=True)
	tahun = models.IntegerField()
	mekanisme_internal = models.TextField()
	mekanisme_eksternal = models.TextField()

class UserProfile(models.Model):
	id_pegawai = models.CharField(max_length=32)
	user = models.OneToOneField(User, null=True, blank=True)
	nama = models.CharField(max_length=32)
	usermane = models.CharField(max_length=32)
	no_hp = models.CharField(max_length=15)
	golongan = models.CharField(max_length=4)
	alamat = models.TextField()
	NIP = models.CharField(max_length=18)
	jenis_user= models.CharField(max_length=32, choices=JENIS_USER)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.nama

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

class Section(models.Model):
	name = models.CharField(max_length = 50)
	
	def __str__(self):
		return self.name
		

class QuestionAnswer(models.Model):
	section = models.ForeignKey(Section)
	question_title = models.CharField(max_length = 128)
	answer = models.TextField()
	
	def __str__(self):      
		return self.question_title
