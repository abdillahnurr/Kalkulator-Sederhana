# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:39:57 2020

@author: Dooo
"""

def kalkulator () :
 def tambah () :
     print ("1.Penjumlahan")
a = input ("Masukkan nilai x = ")
b = input ("Masukkan nilai y = ")
c = a+b
print ("x + y = ", c)
print (" ")
 
 
def kurang () :
    print ("2.Pengurangan")
a = input ("Masukkan nilai x = ")
b = input ("Masukkan nilai y = ")
c = a-b
print ("x - y = ",c)
print (" ")

def kali () :
    print ("3.Perkalian")
a = input ("Masukkan nilai x = ")
b = input ("Masukkan nilai y = ")
c = a*b
print ("x . y = ",c)
print (" ")

def bagi () :
    print ("4.Pembagian")
a = input ("Masukkan nilai x = ")
b = input ("Masukkan nilai y = ")
c = a+b
print ("x /y = ",c)
print (" ")

def pilih () :
    pilih = input("Apakah Anda ingin mengulang (Y/T)? ")
if pilih == ("Y") or pilih == ("y") :
    kalkulator ()
elif pilih == ("T") or choose ("t"):
    print ("Terima kasih sudah menggunakan program ini ^_^")
else :
    print ("Maaf,input yang Anda masukkan salah")
    print ("Silahkan masukkan Y atau T")
    tanya ()
    print ("Program Kalkulator Sederhana")
    print ("################")
    print ("1. Penjumlahan")
    print ("2. Pengurangan")
    print ("3. Perkalian")
    print ("4. Pembagian")
    print ("################")
    print ("silahkan pilih 1-4")
    print (" ")
 
pil = input ("Masukkan pilihan : ")
if pil == "1":
 tambah ()
elif pil == "2":
 kurang ()
elif pil == "3":
 kali ()
elif pil == "4":
 bagi ()
else :
    print ("Maaf, input yang Anda masukkan salah")
tanya ()
kalkulator()