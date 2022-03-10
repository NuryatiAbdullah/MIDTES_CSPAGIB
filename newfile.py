def tugas1():
	print('\n1.')
	
	nilai = {'MTK' : 0, 'IPA' : 0, 'Bhs. Indonesia' : 0}
	
	#input nilai
	for x in nilai:
		nilai[x] = int(input('masukkan nilai %s : ' % x))
	
	#tes kelulusan
	hasil = 'tidak lulus' if all(nilai[key] < 60 for key in nilai) or nilai['MTK'] <= 70 else 'lulus'
	
	print('status kelulusan : %s' % hasil.upper())

def tugas2():
	print('\n2.')
	
	nilai = {'MTK' : 0, 'IPA' : 0, 'Bhs. Indonesia' : 0}
	
	#input nilai
	for key in nilai:
		nilai[key] = int(input('masukkan nilai %s : ' % key))

	#cek nilai yg tidak valid
	for key in nilai:
		if(nilai[key] not in range(0,101)):
			print('maaf input ada yg tidak valid')
			return
	
	#tes kelulusan
	hasil = 'tidak lulus' if all(nilai[key] < 60 for key in nilai) or nilai['MTK'] <= 70 else 'lulus'
	
	print('status kelulusan : %s' % hasil.upper())
	
def tugas3():
	print('\n3.')
	
	nilai = {'MTK' : 0, 'IPA' : 0, 'Bhs. Indonesia' : 0}
	sebab = []
	hasil = ""
	
	#input nilai
	for key in nilai:
		nilai[key] = int(input('masukkan nilai %s : ' % key))

	#cek nilai yg tidak valid
	for key in nilai:
		if(nilai[key] not in range(0,101)):
			print('maaf input ada yg tidak valid')
			return
	
	#tes kelulusan
	for key in nilai:
		if(nilai[key] < 60):
			sebab.append('~ nilai %s kurang dari 60' % key)
	if(nilai['MTK'] <= 70):
		sebab.append('~ nilai matematika kurang dari 70')
	
	hasil = 'LULUS' if len(sebab) == 0 else 'TIDAK LULUS'
	
	print('\nstatus kelulusan : %s\n' % hasil.upper())
	
	#print sebab tidak lulus
	if(hasil == 'TIDAK LULUS'):
		print('sebab :')
		for masalah in sebab:
			print(masalah)

def tugas4():
	print('\n4.')
	
	karyawan = {'kode' : '', 'nama' : '', 'golongan' : ''}
	
	golongan = {'A' : [10000000, 2.5],'B' : [8500000,2.0],'C' : [7000000, 1.5],'D' : [5500000, 1.0]}
	
	for key in karyawan:
		karyawan[key] = input('masukkan %s karyawan : ' % key)
	if(karyawan['golongan'] not in ['A','B','C','D']):
			print('\nmaaf golongan yg anda masukkan tidak ditemukan')
			return	 
	
	#print struk rician karyawan
	gajiPokok = golongan[karyawan['golongan']][0]
	potongan = golongan[karyawan['golongan']][1] * golongan[karyawan['golongan']][0] / 100
	struk = f"""
====================================
STRUK RINCIAN GAJI KARYAWAN
-----------------------------------------------------------
Nama Karyawan			: {karyawan['nama']} (Kode: {karyawan['kode']})
Golongan			: {karyawan['golongan']}
-----------------------------------------------------------
Gaji Pokok			: Rp {'{:,}'.format(gajiPokok)}
Potongan ({golongan[karyawan['golongan']][1]} %)		: Rp {'{:,}'.format(int(potongan))}
----------------------------------------------------------- -
Gaji Bersih			: Rp {'{:,}'.format(int(gajiPokok-potongan))}"""
	print(struk.format(nama=karyawan['nama'],kode=karyawan['kode'],golongan=karyawan['golongan'],gajiPokok=golongan[karyawan['golongan']][0],potongan=golongan[karyawan['golongan']][1],total=()))
	
def tugas5():
	print('\n5.')
	
	karyawan = {'kode' : '', 'nama' : '', 'golongan' : '','status':'','anak':0}
	
	golongan = {'A' : [10000000, 2.5],'B' : [8500000,2.0],'C' : [7000000, 1.5],'D' : [5500000, 1.0]}
	
	for key in karyawan:
		if(key=='status'):
			karyawan['status'] = input('masukkan status (1: menikah, 2: blm) : ')
			if(karyawan['status']=='1'):
				karyawan['anak'] = int(input('masukkan jumlah anak : '))
			break
		karyawan[key] = input('masukkan %s karyawan : ' % key)
	
	if(karyawan['golongan'] not in ['A','B','C','D']):
			print('\nmaaf golongan yg anda masukkan tidak ditemukan')
			return
	
	#print struk rician karyawan
	gajiPokok = golongan[karyawan['golongan']][0]
	tunjanganPasangan = 10 * gajiPokok / 100;
	tunjanganAnak = karyawan['anak'] * (5 * gajiPokok / 100)
	gajiKotor = gajiPokok+tunjanganPasangan+tunjanganAnak
	potongan = golongan[karyawan['golongan']][1] * gajiKotor / 100
	print(f"""
====================================
STRUK RINCIAN GAJI KARYAWAN
-----------------------------------------------------------
Nama Karyawan			: {karyawan['nama']} (Kode: {karyawan['kode']})
Golongan			: {karyawan['golongan']}
Status Menikah			: {({'1':'menikah','2':'blm'}[karyawan['status']])}	
Jumlah Anak			: {karyawan['anak']}		
-----------------------------------------------------------
Gaji Pokok			: Rp {'{:,}'.format(gajiPokok)}
Tunjangan Istri/Suami		: Rp {'{:,}'.format(int(tunjanganPasangan))}
Tunjangan anak			: Rp {'{:,}'.format(int(tunjanganAnak))}
----------------------------------------------------------- +
Gaji Kotor			: Rp {'{:,}'.format(int(gajiKotor))}
Potongan ({golongan[karyawan['golongan']][1]} %)		: Rp {'{:,}'.format(int(potongan))}
----------------------------------------------------------- -
Gaji Bersih			: Rp {'{:,}'.format(int(gajiKotor-potongan))}""")
	
tugas1()
tugas2()
tugas3()
tugas4()
tugas5()