from tkinter import *
import tkinter.messagebox as imsg
# import mysql.connector
# from mysql.connector import Error

# con=mysql.connector.connect(host='localhost',user='root',password='',database='Project',port=3306)

# if con.is_connected():
#     print('Connect Sccussfully')
# else:
#     print('Not connect')
# cursor=con.cursor()

def getval():
    print()
    # name = username.get()
    # p = password.get()
    # a = age.get()
    # phone = mo.get()

    # # Using parameterized query to prevent SQL injection
    # query = "INSERT INTO `Car&Bike Info.`(`UserName`, `Password`, `Age`, `Phone No.`) VALUES (%s, %s, %s, %s)"
    # values = (name, p, a, phone)

    # try:
    #     cursor.execute(query, values)
    #     con.commit()
    #     print("Values Inserted Successfully")
    
    #     # Retrieving ID after successful insertion
    #     cursor.execute(f"SELECT `ID` FROM `car&bike info.` WHERE `Phone No.`={phone}")
    #     sms = (cursor.fetchone())
    #     unboxing=list(sms)
    #     for i in unboxing:
    #         sms=i        # Fetching the ID
    #     imsg.showinfo('info',f'This is Your Id: {sms}\nRemember This,')

    # except mysql.connector.Error as err:
    #     print(f"Error: {err}")
    #     print('Value not inserted')

    # finally:
    #     # Close cursor and connection
    #     cursor.close()
    #     con.close()

def ch():
    vm=choice.get()
    if vm==1:
        s=imsg.showinfo('info','Your Choice is Car')
    elif vm==2:
        s=imsg.showinfo('info','Your Choice is Bike')

def carget():
    cov=br.get()
    imsg.showinfo('info',f'{cov} no index')

        
def rang():
    mv=mysilder1.get()
    mv1=mysilder2.get()
    global mk
    mk=mv
    global mk1
    mk1=mv1
    p=imsg.showinfo('info',f'Your Range Is {mv} to {mv1}')


root=Tk()
root.title("Car & Bike Info System")
root.geometry("1920x1080")

def tab1():
    def tab2():
        ti.destroy()
        l1.destroy()
        l2.destroy()    
        l3.destroy()    
        l4.destroy()
        l5.destroy()
        l6.destroy()
        l7.destroy()
        l8.destroy()
        l9.destroy()
        l10.destroy()
        b1.destroy()
        b2.destroy()
        userentry.destroy()
        passentry.destroy()
        ageentry.destroy()
        moentry.destroy()
        global choice
        choice=IntVar()
        t2l=Label(root,text='What will you choose to Buy :',font='lucida 20 bold',padx=-500)
        t2l.grid(row=5,column=6,padx=500)
        r1=Radiobutton(root,text="Car",padx=30,variable=choice,value=1,font='lucida 15 bold')
        r1.grid(row=6,column=6)
        r2=Radiobutton(root,text="Bike",padx=30,variable=choice,value=2,font='lucida 15 bold')
        r2.grid(row=7,column=6)
        b5=Button(root,text='Submit',bg='green',command=ch)
        b5.grid(row=8,column=6,pady=30)

        # def menu1():
        
        def back():
            t2l.destroy()
            r1.destroy()
            r2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            tab1()

        b3=Button(root,text="Back",fg='black',bg='red',command=back,anchor='nw')
        b3.grid(row=9,column=0,pady=550,padx=10)


        def tab3():
            t2l.destroy()
            r1.destroy()
            r2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            
            l11=Label(root,text='What is Your Range :',font='lucida 20 bold',padx=-500)
            l11.grid(row=5,column=6,padx=500,pady=100)
            
            global mysilder1
            mysilder1=Scale(root,from_=0,to=50000000,orient=HORIZONTAL,length=300)
            mysilder1.set(0)
            mysilder1.grid(row=6,column=6)
            mn=mysilder1.get()
            global mysilder2
            mysilder2=Scale(root,from_=0,to=100000000,orient=HORIZONTAL,length=300)
            mysilder2.set(100000000)
            mysilder2.grid(row=7,column=6)
            mn1=mysilder2.get()
            b6=Button(root,text='Submit',bg='green',command=rang)
            b6.grid(row=8,column=6,pady=30)

            def back1():
                l11.destroy()
                mysilder1.destroy()
                mysilder2.destroy()
                b6.destroy()
                b7.destroy()
                b8.destroy()
                tab2()

            b7=Button(root,text="Back",fg='black',bg='red',command=back1,anchor='nw')
            b7.grid(row=9,column=0,pady=350,padx=10)


            def tab4():
                l11.destroy()
                mysilder1.destroy()
                mysilder2.destroy()
                b6.destroy()
                b7.destroy()
                b8.destroy()

                ca1=IntVar()
                ca2=IntVar()
                ca3=IntVar()
                ca4=IntVar()
                ca5=IntVar()
                bi1=IntVar()
                bi2=IntVar()
                bi3=IntVar()
                bi4=IntVar()
                bi5=IntVar()

                t41=Label(root,text='Choose Your Companay :',font='lucida 20 bold',padx=-500)
                t41.grid(row=5,column=6,padx=500)
                v=choice.get()
                if v==1:
                    c1=Checkbutton(root,text='HONDA',variable=ca1)
                    c1.grid(row=6,column=6)
                    c2=Checkbutton(root,text='MAHINDRA',variable=ca2)
                    c2.grid(row=7,column=6)
                    c3=Checkbutton(root,text='LEMBORGHINI',variable=ca3)
                    c3.grid(row=8,column=6)
                    c4=Checkbutton(root,text='TATA',variable=ca4)
                    c4.grid(row=9,column=6)
                    c5=Checkbutton(root,text='PORSCHE',variable=ca5)
                    c5.grid(row=10,column=6)

                elif v==2:
                    be1=Checkbutton(root,text='KAWASAKI',variable=bi1)
                    be1.grid(row=6,column=6)
                    be2=Checkbutton(root,text='Honda',variable=bi2)
                    be2.grid(row=7,column=6)
                    be3=Checkbutton(root,text='BAJAJ',variable=bi3)
                    be3.grid(row=8,column=6)
                    be4=Checkbutton(root,text='HERO',variable=bi4)
                    be4.grid(row=9,column=6)
                    be5=Checkbutton(root,text='YAMAHA',variable=bi5)
                    be5.grid(row=10,column=6)
                    

                    
                def back3():
                    t41.destroy()
                    if v==1:
                        c1.destroy()
                        c2.destroy()
                        c3.destroy()
                        c4.destroy()
                        c5.destroy()
                    if v==2:
                        be1.destroy()
                        be2.destroy()
                        be3.destroy()
                        be4.destroy()
                        be5.destroy()
                    ba9.destroy()
                    ba1.destroy()
                    tab3()

                ba9=Button(root,text='Back',bg='red',command=back3)
                ba9.grid(row=11,column=1,pady=600,padx=10)

                def tab5():
                    t41.destroy()
                    if v==1:
                        c1.destroy()
                        c2.destroy()
                        c3.destroy()
                        c4.destroy()
                        c5.destroy()
                    if v==2:
                        be1.destroy()
                        be2.destroy()
                        be3.destroy()
                        be4.destroy()
                        be5.destroy()
                    ba9.destroy()
                    ba1.destroy()
                      
                    v1=ca1.get()
                    v2=ca2.get()
                    v3=ca3.get()
                    v4=ca4.get()
                    v5=ca5.get()
                    x1=bi1.get()
                    x2=bi2.get()
                    x3=bi3.get()
                    x4=bi4.get()
                    x5=bi5.get()


                    m=choice.get()
                    if m==1:
                        l51=Label(root,text='Your Recommended Car : ',font='lucida 20 bold')
                        l51.grid(row=5,column=6,padx=475)
                    elif m==2:
                        l52=Label(root,text='Your Recommended Bike : ',font='lucida 20 bold')
                        l52.grid(row=5,column=6,padx=475)


                    f1=Frame(root,borderwidth=20,relief=SUNKEN)
                    f1.grid(row=6,column=6)
                    
                    
                    HONDA={"CITY":{"Company Name":"HONDA","Milage":"18-19 kmpl","Power":"119.3 bhp","Engine":"1498 cc","Fual":"Petrol","Variants-price":{"SV":1171000,"V":1262000,"V CTV":1384000,"VX":1371000,"VX CTV":1496000,"ZX":1494000,"ZX CTV":1619000}},
                            "AMAZE":{"Company Name":"HONDA","Milage":"17-18 kmpl","Power":"88.5 bhp","Engine":"1199 cc","Fual":"Petrol","Variants-price":{"E":716000,"S":784000,"S CTV":873000,"VX":895000,"Elite Adition":910000,"VX CTV":977000,"Elite Adition CTV":992000}},
                            "ELEVATE":{"Company Name":"HONDA","Milage":"15-17 kmpl","Power":"119.3 bhp","Engine":"1498 cc","Fual":"Petrol","Variants-price":{"SV":1158000,"V":1231000,"V CTV":1341000,"VX":1370000,"VX CTV":1480000,"ZX":1510000,"ZX CTV":1620000}}}
                    MAHINDRA={"XUV700":{"Company Name":"MAHINDRA","Milage":"16-17 kmpl","Power":"152.87-197.13 bhp","Engine":"1999-2198 cc","Fual":"Petrol/Diesel","Variants-price":{"MX":1399000,"MX Diesel":1459000,"AX3":1699000,"AX5 AT ":1949000,"AX5 AT Diesel":2009000,"AX7 AT LUXURY PACK":2529000,"AX7 Diesel AT LUXURY PACK":2699000}},
                                "THAR":{"Company Name":"MAHINDRA","Milage":"15.7 kmpl","Power":"116.87-150.13 bhp","Engine":"1497-2184 cc","Fual":"Petrol/Diesel","Variants-price":{"LX AT HARD TOP Diesel":1720000,"LX AT CONVERT TOP Diesel":1715000,"LX HARD TOP ":1500000,"LX HARD TOP Diesel MLD":1555000,"Earth Edition ":1540000,"Earth Edition AT":1700000,"Earth Edition Diesel AT":1760000}},
                                "SCORPIO":{"Company Name":"MAHINDRA","Milage":"15-16 kmpl","Power":"130 bhp","Engine":"2184 cc","Fual":"Petrol/Diesel","Variants-price":{"N Z2 MT 7 STR":1360000,"N Z2 Diesel MT 7 STR":1400000,"S Diesel":1359000,"S 9 STR Diesel":1384000,"S 11 Diesel":1735000,"S 11 7CC Diesel":1735000,"N Z8 L Diesel AT 2WD 7 STR":2224000}}}
                    LAMBORGHINI={"URUS":{"Company Name":"LAMBORGHINI","Milage":"6-7 kmpl","Power":"657 bhp","Engine":"3996 cc","Fual":"Petrol","Variants-price":{"Performante":42200000,"S":41800000}},
                                "HURACAN":{"Company Name":"LAMBORGHINI","Milage":"6-7 kmpl","Power":"571-859 bhp","Engine":"5204 cc","Fual":"Petrol","Variants-price":{"EVO":32200000,"EVO SPYDER":35400000,"STO":49900000,"TECNICA":40400000,"STERRATO":46100000}},
                                "REVUELTO":{"Company Name":"LAMBORGHINI","Milage":"5-6 kmpl","Power":"814 bhp","Engine":"6498 cc","Fual":"HYBRID","Variants-price":{"LB 744":88900000}}}
                    TATA={"PUNCH":{"Company Name":"TATA","Milage":"18-20 kmpl","Power":"72.41-86.63 bhp","Engine":"1199 cc","Fual":"Petrol/CNG","Variants-price":{"ADVENTURE RHYTHM":735000,"VADVENTURE RHYTHM AMT":795000,"ADVENTURE RHYTHM CNG":1384000,"ADVENTURE CNG":1371000,"CREATIVE S DT":930000,"ACCOMPLISHED DAZZLE S CNG":985000,"CREATIVE FLAGSHIP AMT DT":1020000}},
                            "HARRIER":{"Company Name":"TATA","Milage":"16-17 kmpl","Power":"167.62 bhp","Engine":"1956 cc","Fual":"Diesel","Variants-price":{"SMART(O)":1549000,"PURE(O)":795000,"PURE PLUS AT":1999000,"PURE PLUS S DARK":1999000,"ADVANTURE PLUS":2169000,"FEARLESS":2299000,"FEARLESS PLUS DARK AT":2644000}},
                            "NEXON":{"Company Name":"TATA","Milage":"17-24 kmpl","Power":"113.3-118.3 bhp","Engine":"1199-1498 cc","Fual":"Petrol/Diesel","Variants-price":{"SMART":815000,"CREATIVE PLUS S DARK Diesel AMT":1475000,"FEARLESS PLUS S DT DCA":1480000,"FEARLESS PLUS S DT Diesel":1500000,"FEARLESS DARK Diesel AMT":1505000,"FEARLESS PR PLUS S DT Diesel AMT":1560000,"FEARLESS PLUS S DARK Diesel":1518000}},}
                    PORSCHE={"MACAN":{"Company Name":"PORSCHE","Milage":"10-11 kmpl","Power":"241-434 bhp","Engine":"1984-2894 cc","Fual":"Petrol","Variants-price":{"BASE":8806000,"S":14400000,"GTS":15300000}},
                                "991":{"Company Name":"PORSCHE","Milage":"7-11 kmpl","Power":"380-641 bhp","Engine":"2981-3996 cc","Fual":"Petrol","Variants-price":{"CARRERA":18600000,"CARRERA T":19400000,"GT3":27500000,"TURBO S":33500000,"S/T":42600000}},
                                 "CAYENNE":{"Company Name":"PORSCHE","Milage":"8-41 kmpl","Power":"348 bhp","Engine":"2995 cc","Fual":"Petrol","Variants-price":{"BASE":13600000,"COUPE BASE":14200000}},}
                    KAWASAKI={"Z900":{"Company Name":"KAWASAKI","Milage":"15 kmpl","Power":"123.64 bhp","Engine":"948 cc","Fual Tank Capacity":"17 L","Kerb Weight":"212 kg","Fual":"Petrol","Variants-price":{"STANDARD":929000}},
                                "NINJA 300":{"Company Name":"KAWASAKI","Milage":"29 kmpl","Power":"38.88 bhp","Engine":"296 cc","Fual Tank Capacity":"17 L","Kerb Weight":"179 kg","Fual":"Petrol","Variants-price":{"STANDARD":343000}},
                                "NINJA 500":{"Company Name":"KAWASAKI","Milage":"22 kmpl","Power":"44.7 bhp","Engine":"451 cc","Fual Tank Capacity":"14 L","Kerb Weight":"171 kg","Fual":"Petrol","Variants-price":{"STANDARD":525000}},
                                "NINJA ZX-6R":{"Company Name":"KAWASAKI","Milage":"18 kmpl","Power":"122.07 bhp","Engine":"636 cc","Fual Tank Capacity":"17 L","Kerb Weight":"198 kg","Fual":"Petrol","Variants-price":{"STANDARD":1109000}},
                                "Z650":{"Company Name":"KAWASAKI","Milage":"16 kmpl","Power":"67.31 bhp","Engine":"649 cc","Fual Tank Capacity":"15 L","Kerb Weight":"191 kg","Fual":"Petrol","Variants-price":{"STANDARD":665000}},
                                "NINJA ZX-10R":{"Company Name":"KAWASAKI","Milage":"15 kmpl","Power":"200.21 bhp","Engine":"998 cc","Fual Tank Capacity":"17 L","Kerb Weight":"207 kg","Fual":"Petrol","Variants-price":{"STANDARD":1663000}},
                                "NINJA 650":{"Company Name":"KAWASAKI","Milage":"30 kmpl","Power":"67.3 bhp","Engine":"649 cc","Fual Tank Capacity":"15 L","Kerb Weight":"196 kg","Fual":"Petrol","Variants-price":{"STANDARD":716000}},
                                "NINJA 400":{"Company Name":"KAWASAKI","Milage":"32 kmpl","Power":"44.7 bhp","Engine":"399 cc","Fual Tank Capacity":"14 L","Kerb Weight":"168 kg","Fual":"Petrol","Variants-price":{"STANDARD":523985}},
                                "VULCAN S":{"Company Name":"KAWASAKI","Milage":"19 kmpl","Power":"59.94 bhp","Engine":"649 cc","Fual Tank Capacity":"14 L","Kerb Weight":"235 kg","Fual":"Petrol","Variants-price":{"STANDARD":710000}},
                                "NINJA H2 SX":{"Company Name":"KAWASAKI","Milage":"9 kmpl","Power":"197.2 bhp","Engine":"998 cc","Fual Tank Capacity":"19 L","Kerb Weight":"266 kg","Fual":"Petrol","Variants-price":{"STANDARD":3195000}}}
                    Honda={"SP 125":{"Company Name":"HONDA","Milage":"65 kmpl","Power":"10.72 bhp","Engine":"124 cc","Fual Tank Capacity":"11.2 L","Kerb Weight":"116 kg","Fual":"Petrol","Variants-price":{"DRUM":86747,"DISC":90747,"SPORT EDITION":91298}},
                            "SP 160":{"Company Name":"HONDA","Milage":"50 kmpl","Power":"13.27 bhp","Engine":"162.71 cc","Fual Tank Capacity":"12 L","Kerb Weight":"139 kg","Fual":"Petrol","Variants-price":{"SINGLE DISC":118092,"DOUBLE DISC":122492}},
                            "ACTIVA 6G":{"Company Name":"HONDA","Milage":"47 kmpl","Power":"7.73 bhp","Engine":"109.51 cc","Fual Tank Capacity":"5.3 L","Kerb Weight":"106 kg","Fual":"Petrol","Variants-price":{"STANDARD":77712,"DELUXE":80212,"DELUXE-LIMITED EDITION":82211,"H-SMART":83703}},
                            "SHINE 125":{"Company Name":"HONDA","Milage":"55 kmpl","Power":"10.59 bhp","Engine":"123.94 cc","Fual Tank Capacity":"10.5 L","Kerb Weight":"113 kg","Fual":"Petrol","Variants-price":{"DRUM":80409,"DISC":84409}},
                            "UNICORN":{"Company Name":"HONDA","Milage":"50 kmpl","Power":"12.73 bhp","Engine":"162.7 cc","Fual Tank Capacity":"13 L","Kerb Weight":"140 kg","Fual":"Petrol","Variants-price":{"STANDARD":109679}},
                            "HORNET 2.0":{"Company Name":"HONDA","Milage":"45 kmpl","Power":"17.03 bhp","Engine":"184.4 cc","Fual Tank Capacity":"12 L","Kerb Weight":"142 kg","Fual":"Petrol","Variants-price":{"STANDARD":139000,"REPSOL EDITION":140000}},
                            "SHINE 100":{"Company Name":"HONDA","Milage":"65 kmpl","Power":"7.28 bhp","Engine":"98.98 cc","Fual Tank Capacity":"9 L","Kerb Weight":"99 kg","Fual":"Petrol","Variants-price":{"STANDARD":65011}},
                            "DIO":{"Company Name":"HONDA","Milage":"48 kmpl","Power":"7.75 bhp","Engine":"109.51 cc","Fual Tank Capacity":"5.3 L","Kerb Weight":"103 kg","Fual":"Petrol","Variants-price":{"STANDARD":74235,"DELUXE":78236,"H-SMART":81736}},
                            "LIVO":{"Company Name":"HONDA","Milage":"60 kmpl","Power":"8.67 bhp","Engine":"109.51 cc","Fual Tank Capacity":"9 L","Kerb Weight":"113 kg","Fual":"Petrol","Variants-price":{"DRUM":78826,"DISC":82826}},
                            "CB300F":{"Company Name":"HONDA","Milage":"34 kmpl","Power":"24.13 bhp","Engine":"293.51 cc","Fual Tank Capacity":"14.1 L","Kerb Weight":"153 kg","Fual":"Petrol","Variants-price":{"STANDARD":170150}},
                            "GOLDWING TOUR":{"Company Name":"HONDA","Milage":"7 kmpl","Power":"124.7 bhp","Engine":"1833 cc","Fual Tank Capacity":"21.1 L","Kerb Weight":"390 kg","Fual":"Power Petrol","Variants-price":{"STANDARD":3989985}}}
                    BAJAJ={"PULSER NS200":{"Company Name":"BAJAJ","Milage":"36 kmpl","Power":"24.13 bhp","Engine":"199.5 cc","Fual Tank Capacity":"12 L","Kerb Weight":"159 kg","Fual":"Petrol","Variants-price":{"SINGLE CHANNEL ABS":142055,"DUAL CHANNEL ABS":150591,"BLUETOOTH":157913}},
                            "PULSER N160":{"Company Name":"BAJAJ","Milage":"51 kmpl","Power":"15.68 bhp","Engine":"164.5 cc","Fual Tank Capacity":"14 L","Kerb Weight":"152 kg","Fual":"Petrol","Variants-price":{"SINGLE CHANNEL ABS":122959,"DUAL CHANNEL ABS":130524,"DUAL CHANNEL ABS[2024]":133013}},
                            "PULSER RS200":{"Company Name":"BAJAJ","Milage":"35 kmpl","Power":"24.1 bhp","Engine":"199.5 cc","Fual Tank Capacity":"13 L","Kerb Weight":"166 kg","Fual":"Petrol","Variants-price":{"STANDARD":171914}},
                            "DOMINAR 400":{"Company Name":"BAJAJ","Milage":"29 kmpl","Power":"39.42 bhp","Engine":"373.3 cc","Fual Tank Capacity":"13 L","Kerb Weight":"193 kg","Fual":"Power Petrol","Variants-price":{"TOURING":224676}},
                            "PLATINA 100":{"Company Name":"BAJAJ","Milage":"72 kmpl","Power":"7.79 bhp","Engine":"102 cc","Fual Tank Capacity":"11 L","Kerb Weight":"117 kg","Fual":"Petrol","Variants-price":{"KS DRUM":61617,"ES DRUM":66119}},
                            "CHETAK EV":{"Company Name":"BAJAJ","Fual":"ELECTRIC","Driving Range":"108-126 km","Battry Charging Time":"4 h 50 m","Top Speed":"63 kmph","Variants-price":{"URBANE TECPEC[2024]":124562,"PREMIUM TECPEC[2024]":144566,"URBANE STANDARD[2024]":117294,"PREMIUM EDITION[2024]":143379,"PREMIUM[2024]":137687}},
                            "CT 125X":{"Company Name":"BAJAJ","Milage":"60 kmpl","Power":"10.7 bhp","Engine":"124.4 cc","Fual Tank Capacity":"11 L","Kerb Weight":"130 kg","Fual":"Petrol","Variants-price":{"DRUM":73611,"DISC":76816}},
                            "AVENGER STREET 160":{"Company Name":"BAJAJ","Milage":"45 kmpl","Power":"14.79 bhp","Engine":"160 cc","Fual Tank Capacity":"13 L","Kerb Weight":"156 kg","Fual":"Petrol","Variants-price":{"STANDARD":114640}},
                            "PLUSER 220F":{"Company Name":"BAJAJ","Milage":"40 kmpl","Power":"20.11 bhp","Engine":"220 cc","Fual Tank Capacity":"15 L","Kerb Weight":"160 kg","Fual":"Petrol","Variants-price":{"STANDARD":138285}},
                            "PLUSER F250":{"Company Name":"BAJAJ","Milage":"38 kmpl","Power":"24.1 bhp","Engine":"249 cc","Fual Tank Capacity":"14 L","Kerb Weight":"164 kg","Fual":"Petrol","Variants-price":{"DUAL CHANNEL ABS":150451}}}
                    HERO={"XTREME 125R":{"Company Name":"HERO","Milage":"60 kmpl","Power":"11.4 bhp","Engine":"124.7 cc","Fual Tank Capacity":"10 L","Kerb Weight":"136 kg","Fual":"Petrol","Variants-price":{"IBS":96786,"SINGLE CHANNEL ABS":102142}},
                            "SPLENDOR PLUS":{"Company Name":"HERO","Milage":"60 kmpl","Power":"7.91 bhp","Engine":"97.2 cc","Fual Tank Capacity":"9.8 L","Kerb Weight":"112 kg","Fual":"Petrol","Variants-price":{"SELF ALLOY":73441,"BLACK AND ACCENT EDITION":74557,"SELF ALLOY i3S":74637}},
                            "HF DELUXE":{"Company Name":"HERO","Milage":"65 kmpl","Power":"7.91 bhp","Engine":"97.2 cc","Fual Tank Capacity":"9.1 L","Kerb Weight":"110 kg","Fual":"Petrol","Variants-price":{"SELF ALLOY":66516,"KICK ALLOY":61163,"DRUM SELF ALLOY BLACK":67881,"SELF ALLOY i3S":66165}},
                            "GLAMOUR XTEC":{"Company Name":"HERO","Milage":"55 kmpl","Power":"10.72 bhp","Engine":"124.7 cc","Fual Tank Capacity":"10 L","Kerb Weight":"122 kg","Fual":"Petrol","Variants-price":{"DRUM ALLOY":88048,"DISC ALLOY":92653}},
                            "KARIZMA XMR":{"Company Name":"HERO","Milage":"35 kmpl","Power":"25.15 bhp","Engine":"210 cc","Fual Tank Capacity":"11 L","Kerb Weight":"163.5 kg","Fual":"Petrol","Variants-price":{"STANDARD":179900}},
                            "PLESURE +":{"Company Name":"HERO","Milage":"50 kmpl","Power":"8 bhp","Engine":"110 cc","Fual Tank Capacity":"4.8 L","Kerb Weight":"104 kg","Fual":"Petrol","Variants-price":{"LX":70322,"VX":73765}},
                            "XTREME 160R 4V":{"Company Name":"HERO","Milage":"45 kmpl","Power":"16.4 bhp","Engine":"163.27 cc","Fual Tank Capacity":"12 L","Kerb Weight":"144 kg","Fual":"Petrol","Variants-price":{"DOUBLE DISC":128492,"DOUBLE DISC CONNECTED":133964,"PREMIUM":137636}},
                            "SUPER SPLANDOR XTEC":{"Company Name":"HERO","Milage":"60 kmpl","Power":"10.72 bhp","Engine":"124.7 cc","Fual Tank Capacity":"12 L","Kerb Weight":"144 kg","Fual":"Petrol","Variants-price":{"DOUBLE DISC":128492,"DOUBLE DISC CONNECTED":133964,"PREMIUM":137636}},
                            "PASSION XTEC":{"Company Name":"HERO","Milage":"58 kmpl","Power":"7.72 bhp","Engine":"113.2 cc","Fual Tank Capacity":"10 L","Kerb Weight":"117 kg","Fual":"Petrol","Variants-price":{"DISC ALLOY":84482,"DRUM ALLOY":80701}}}
                    YAMAHA={"MT 15 V2":{"Company Name":"YAMAHA","Milage":"48 kmpl","Power":"18.1 bhp","Engine":"155 cc","Fual Tank Capacity":"10 L","Kerb Weight":"141 kg","Fual":"Petrol","Variants-price":{"STANDARD":168708,"DELUXE":172708,"MOTO GP EDITION":174208}},
                            "R15 V4":{"Company Name":"YAMAHA","Milage":"45 kmpl","Power":"18.91 bhp","Engine":"155 cc","Fual Tank Capacity":"11 L","Kerb Weight":"141 kg","Fual":"Petrol","Variants-price":{"SEMETALIC RED":182854,"DARK KNIGHT":183854,"M":197054}},
                            "FZ Fi V4":{"Company Name":"YAMAHA","Milage":"49 kmpl","Power":"12.2 bhp","Engine":"149 cc","Fual Tank Capacity":"13 L","Kerb Weight":"136 kg","Fual":"Petrol","Variants-price":{"STANDARD":129780,"DELUXE":130279}},
                            "AEROX 155":{"Company Name":"YAMAHA","Milage":"40 kmpl","Power":"14.2 bhp","Engine":"155 cc","Fual Tank Capacity":"5.5 L","Kerb Weight":"126 kg","Fual":"Petrol","Variants-price":{"STANDARD":148072,"MOTO GP EDITION":149575}},
                            "MT-03":{"Company Name":"YAMAHA","Milage":"26 kmpl","Power":"41.5 bhp","Engine":"321 cc","Fual Tank Capacity":"14 L","Kerb Weight":"153.5 kg","Fual":"Petrol","Variants-price":{"STANDARD":460259}},
                            "RAY ZR 125":{"Company Name":"YAMAHA","Milage":"51 kmpl","Power":"8.04 bhp","Engine":"125 cc","Fual Tank Capacity":"5.2 L","Kerb Weight":"99 kg","Fual":"Petrol","Variants-price":{"RACING BLUE AND DARK MATTE BLUE":94076,"STREET RALLY-MATTE COPPER":97076}}}
                    
                    carname=[]
                    bikename=[]
                    allcar=["CITY","AMAZE","ELEVATE","XUV700","THAR","SCORPIO","URUS","HURACAN","REVUELTO","PUNCH","HARRIER","NEXON","MACAN","991","CAYENNE"]
                    allbike=["Z900","NINJA 300","NINJA 500","NINJA ZX-6R","Z650","NINJA ZX-19R","NINJA 650","NINJA 400","VULCAN S","NINJA H2 SX","SP 125"
                             ,"SP 160","ACTIVA 6G","SHINE 125","UNICORN","HORNET 2.0","SHINE 100","DIO","LIVO","CB300F","GOLDWING TOUR","PULSER NS200","PULSER N160"
                             ,"PULSER RS200","DOMINAR 400","PLATINA 100","CHETAK EV","CT 125X","AVENGER STREET 160","PLUSER 220F","PLUSER F250","XTREME 125R","SPLENDOR PLUS"
                             ,"HF DELUXE","GLAMOUR XTEC","KARIZMA XMR","PLESURE +","XTREME 160R 4V","SUPER SPLANDOR XTEC","PASSION XTEC","MT 15 V2","R15 V4","FZ Fi V4"
                             ,"AEROX 155","MT-03","RAY ZR 125"]
                    
                    # print(mk,mk1)
                    # print(v1,v2,v3,v4,v5)
                    # print(x1,x2,x3,x4,x5)
                    car=[]
                    bike=[]
                    if(v1==1):
                        car.append(HONDA)
                        carname.append('HONDA')

                    if(v2==1):
                        car.append(MAHINDRA)
                        carname.append('MAHINDRA')

                    if(v3==1):
                        car.append(LAMBORGHINI)
                        carname.append('LAMBORGHINI')

                    if(v4==1):
                        car.append(TATA)
                        carname.append('TATA')

                    if(v5==1):
                        car.append(PORSCHE)
                        carname.append('PORSCHE')
                    if(x1==1):
                        bike.append(KAWASAKI)
                        bikename.append('KAWASAKI')
                    if(x2==1):
                        bike.append(Honda)
                        bikename.append('Honda')
                    if(x3==1):
                        bike.append(BAJAJ)
                        bikename.append('BAJAJ')
                    if(x4==1):
                        bike.append(HERO)
                        bikename.append('HERO')
                    if(x5==1):
                        bike.append(YAMAHA)
                        bikename.append('YAMAHA')

                    # print(car)
                    global br
                    br=IntVar()
                    countv=0
                    countv1=0
                    countv2=0
                    carran=[]
                    bikeran=[]
                    variables1 = {}
                    variables2 = {}
                    variables5 = {}
                    variables4 = {}

                    if(m==1):
                        for i in range(len(car)):
                            for o in car[i].keys():                       
                                nh=car[i]
                                for k,l in nh[o]['Variants-price'].items():
                                    # print(o)
                                    if(o not in carran):
                                        variables1[f"ca{countv}"] = IntVar()
                                        if(mk<l<mk1):
                                        
                                            if(countv<16):
                                                variables2[f'check{countv}']= Checkbutton(f1,text=f'{o}',variable=variables1[f"ca{countv}"])
                                                variables2[f'check{countv}'].grid(row=countv,column=0)
                                                carran.append(o)
                                                countv+=1
                                            else:
                                                if(countv1<16): 
                                                    variables2[f'check{countv}']= Checkbutton(f1,text=f'{o}',variable=variables1[f"ca{countv}"])
                                                    variables2[f'check{countv}'].grid(row=countv1,column=2,padx=10)
                                                    countv1+=1
                                                    carran.append(o)
                                                    countv+=1

                                                else:
                                                    if(countv2<16):
                                                        variables2[f'check{countv}']=Checkbutton(f1,text=f'{o}',variable=variables1[f"ca{countv}"])
                                                        variables2[f'check{countv}'].grid(row=countv2,column=4,padx=10)
                                                        countv2+=1
                                                        carran.append(o)
                                                        countv+=1

                                            
                                
                    elif(m==2):
                        for i in range(len(bike)):
                            for o in bike[i].keys():
                                        
                                nh=bike[i]
                                for k,l in nh[o]['Variants-price'].items():
                                    # print(o)
                                    if(o not in bikeran):
                                        variables4[f"bv{countv}"] = IntVar()
                                        if(mk<l<mk1):
                                        
                                            if(countv<16):
                                                    
                                                variables5[f"bike{countv}"]= Checkbutton(f1,text=f'{o}',variable=variables4[f"bv{countv}"])
                                                variables5[f"bike{countv}"].grid(row=countv,column=0)
                                                bikeran.append(o)
                                                countv+=1
                                            else:
                                                if(countv1<16): 
                                                    variables5[f"bike{countv}"]= Checkbutton(f1,text=f'{o}',variable=variables4[f"bv{countv}"])
                                                    variables5[f"bike{countv}"].grid(row=countv1,column=2,padx=10)
                                                    countv1+=1
                                                    bikeran.append(o)
                                                    countv+=1

                                                else:
                                                    if(countv2<16):
                                                        variables5[f"bike{countv}"]=Checkbutton(f1,text=f'{o}',variable=variables4[f"bv{countv}"])
                                                        variables5[f"bike{countv}"].grid(row=countv2,column=4,padx=10)
                                                        countv2+=1
                                                        bikeran.append(o)
                                                        countv+=1

                                            
                               
                                    
                    # print(carran)
                    # print(bikeran)
                    def back4():
                        if m==1:
                            l51.destroy()
                        elif m==2:
                            l52.destroy()
                        f1.destroy()
                    
                        countv=0
                        countv1=0
                        countv2=0
                        if(m==1):
                            for i in range(len(car)):
                                for o in car[i].keys():
                                        
                                    nh=car[i]
                                    for k,l in nh[o]['Variants-price'].items():
                                        # print(o)
                                        if(o not in carran):
                                        
                                            if(mk<l<mk1):
                                        
                                                if(countv<16):
                                                
                                                    variables2[f'check{countv}'].destroy()
                                                    countv+=1
                                                
                                                else:
                                                    if(countv1<16): 
                                                        variables2[f'check{countv}'].destroy()
                                                        countv1+=1
                                                        countv+=1
                                                    

                                                    else:
                                                        if(countv2<16):
                                                            variables2[f'check{countv}'].destroy()
                                                            countv2+=1
                                                            countv+=1
                                                        

                                                                                
                                                
                        elif(m==2):
                            for i in range(len(car)):
                                for o in car[i].keys():
                                        
                                    nh=car[i]
                                    for k,l in nh[o]['Variants-price'].items():
                                        # print(o)
                                        if(o not in carran):
                                        
                                            if(mk<l<mk1):
                                        
                                                if(countv<16):
                                                
                                                    variables5[f"bike{countv}"].destroy()
                                                    countv+=1
                                                
                                                else:
                                                    if(countv1<16): 
                                                        variables5[f"bike{countv}"].destroy()
                                                        countv1+=1
                                                        countv+=1
                                                    

                                                    else:
                                                        if(countv2<16):
                                                            variables5[f"bike{countv}"].destroy()
                                                            countv2+=1
                                                            countv+=1                                               
                        b51.destroy()
                        b52.destroy()
                        tab4()

                    b51=Button(root,text='Back',bg='red',command=back4)
                    b51.grid(row=11,column=1,pady=290,padx=10)

                    def tab6():
                        if m==1:
                            l51.destroy()
                        elif m==2:
                            l52.destroy()
                        f1.destroy()
                        countv=0
                        countv1=0
                        countv2=0

                        if(m==1):
                            for i in range(len(car)):
                                for o in car[i].keys():
                                        
                                    nh=car[i]
                                    for k,l in nh[o]['Variants-price'].items():
                                        # print(o)
                                        if(o not in carran):
                                        
                                            if(mk<l<mk1):
                                        
                                                if(countv<16):
                                                
                                                    variables2[f'check{countv}'].destroy()
                                                    countv+=1
                                                
                                                else:
                                                    if(countv1<16): 
                                                        variables2[f'check{countv}'].destroy()
                                                        countv1+=1
                                                        countv+=1
                                                    

                                                    else:
                                                        if(countv2<16):
                                                            variables2[f'check{countv}'].destroy()
                                                            countv2+=1
                                                            countv+=1

                        elif(m==2):
                            for i in range(len(car)):
                                for o in car[i].keys():
                                        
                                    nh=car[i]
                                    for k,l in nh[o]['Variants-price'].items():
                                        # print(o)
                                        if(o not in carran):
                                        
                                            if(mk<l<mk1):
                                        
                                                if(countv<16):
                                                
                                                    variables5[f"bike{countv}"].destroy()
                                                    countv+=1
                                                
                                                else:
                                                    if(countv1<16): 
                                                        variables5[f"bike{countv}"].destroy()
                                                        countv1+=1
                                                        countv+=1
                                                    

                                                    else:
                                                        if(countv2<16):
                                                            variables5[f"bike{countv}"].destroy()
                                                            countv2+=1
                                                            countv+=1
                                                               
                        b51.destroy()
                        b52.destroy()

                        cv=0
                        cv1=0
                        cv2=0
                        cv3=0
                        if(m==1):
                            t61=Label(root,text="Car's Variants :",font='lucida 20 bold')
                            t61.grid(row=5,column=6,padx=550)
                        elif(m==2):
                            t61=Label(root,text="Bike's Variants :",font='lucida 20 bold')
                            t61.grid(row=5,column=6,padx=550)

                        f2=Frame(root,borderwidth=20,relief=SUNKEN)
                        f2.grid(row=6,column=6)
                        vbr=IntVar()
                        selectcar={}
                        variables3={}
                        variables6={}
                        veriofc=[]
                        veriofcn=[]
                        veriofb=[]
                        veriofbn=[]
                        verishowb={}
                        variant=[]

                        if(m==1):
                            for i in range(len(variables1)):
                                if(variables1[f"ca{i}"].get()==1):
                                    # selectcar[carran[i]]=variables1[f"ca{i}"].get()
                                    variant.append(carran[i])
                        elif(m==2):
                            for i in range(len(variables4)):
                                if(variables4[f"bv{i}"].get()==1):
                                    # selectcar[carran[i]]=variables1[f"ca{i}"].get()
                                    variant.append(bikeran[i])

                        
                        if(m==1):
                            for i in range(15):
                                if(len(variant)!=15):
                                    variant.append('')
                        elif(m==2):
                            for i in range(46):
                                if(len(variant)!=46):
                                    variant.append('')
                        # print(variant)
                        # print(len(car))
                        # print(len(bike))
                        if(m==1):
                            for i in range(15):
                                if('HONDA' in carname):
                                    for j in range(0,3):
                                        cm=allcar[j]
                                        if(variant[i]==cm):
                                            for k,l in HONDA[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):
                                                        variables3[f'svariant{cv}']=Radiobutton(f2,text=f'HONDA {cm} {k}',variable=vbr,value=cv)
                                                        variables3[f'svariant{cv}'].grid(row=cv,column=0)
                                                        veriofc.append(k)
                                                        veriofcn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables3[f'svariant{cv}']=Radiobutton(f2,text=f'HONDA {cm} {k}',variable=vbr,value=cv)
                                                            variables3[f'svariant{cv}'].grid(row=cv1,column=2,padx=10)
                                                            
                                                            veriofc.append(k)
                                                            veriofcn.append(cm)
                                                            cv1+=1
                                                            cv+=1

                                                        else:
                                                            if(cv2<28):
                                                                variables3[f'svariant{cv}']=Radiobutton(f2,text=f'HONDA {cm} {k}',variable=vbr,value=cv)
                                                                variables3[f'svariant{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofc.append(k)
                                                                veriofcn.append(cm)

                                                                cv2+=1
                                                                cv+=1

                                                    
                                                    
                                if('MAHINDRA' in carname):
                                    for j in range(3,6):
                                        cm=allcar[j]
                                        if(variant[i]==cm):
                                            for k,l in MAHINDRA[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables3[f'svariant{cv}']=Radiobutton(f2,text=f'MAHINDRA {cm} {k}',variable=vbr,value=cv)
                                                        variables3[f'svariant{cv}'].grid(row=cv,column=0)
                                                        veriofc.append(k)
                                                        veriofcn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables3[f'svariant{cv}']=Radiobutton(f2,text=f'MAHINDRA {cm} {k}',variable=vbr,value=cv)
                                                            variables3[f'svariant{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofc.append(k)
                                                            veriofcn.append(cm)

                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables3[f'svariant{cv}']=Radiobutton(f2,text=f'MAHINDRA {cm} {k}',variable=vbr,value=cv)
                                                                variables3[f'svariant{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofc.append(k)
                                                                veriofcn.append(cm)

                                                                cv2+=1
                                                                cv+=1

                                                    
                                                    
                                if('LAMBORGHINI' in carname):
                                    for j in range(6,9):
                                        cm=allcar[j]
                                        if(variant[i]==cm):
                                            for k,l in LAMBORGHINI[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables3[f'svariant{cv}']=Radiobutton(f2,text=f'LAMBORGHINI {cm} {k}',variable=vbr,value=cv)
                                                        variables3[f'svariant{cv}'].grid(row=cv,column=0)
                                                        veriofc.append(k)
                                                        veriofcn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables3[f'svariant{cv}']=Radiobutton(f2,text=f'LAMBORGHINI {cm} {k}',variable=vbr,value=cv)
                                                            variables3[f'svariant{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofc.append(k)
                                                            veriofcn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables3[f'svariant{cv}']=Radiobutton(f2,text=f'LAMBORGHINI {cm} {k}',variable=vbr,value=cv)
                                                                variables3[f'svariant{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofc.append(k)
                                                                veriofcn.append(cm)
                                                                cv2+=1
                                                                cv+=1

                                                    
                                                    
                                if('TATA' in carname):
                                    for j in range(9,12):
                                        cm=allcar[j]
                                        if(variant[i]==cm):
                                            for k,l in TATA[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables3[f'svariant{cv}']=Radiobutton(f2,text=f'TATA {cm} {k}',variable=vbr,value=cv)
                                                        variables3[f'svariant{cv}'].grid(row=cv,column=0)
                                                        veriofc.append(k)
                                                        veriofcn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables3[f'svariant{cv}']=Radiobutton(f2,text=f'TATA {cm} {k}',variable=vbr,value=cv)
                                                            variables3[f'svariant{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofc.append(k)
                                                            veriofcn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables3[f'svariant{cv}']=Radiobutton(f2,text=f'TATA {cm} {k}',variable=vbr,value=cv)
                                                                variables3[f'svariant{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofc.append(k)
                                                                veriofcn.append(cm)
                                                                cv2+=1
                                                                cv+=1

                                                    
                                                    
                                if('PORSCHE' in carname):
                                    for j in range(12,15):
                                        cm=allcar[j]
                                        if(variant[i]==cm):
                                            for k,l in PORSCHE[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                                        
                                                        variables3[f'svariant{cv}']=Radiobutton(f2,text=f'PORSCHE {cm} {k}',variable=vbr,value=cv)
                                                        variables3[f'svariant{cv}'].grid(row=cv,column=0)
                                                        veriofc.append(k)
                                                        veriofcn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables3[f'svariant{cv}']=Radiobutton(f2,text=f'PORSCHE {cm} {k}',variable=vbr,value=cv)
                                                            variables3[f'svariant{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofc.append(k)
                                                            veriofcn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables3[f'svariant{cv}']=Radiobutton(f2,text=f'PORSCHE {cm} {k}',variable=vbr,value=cv)
                                                                variables3[f'svariant{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofc.append(k)
                                                                veriofcn.append(cm)
                                                                cv2+=1
                                                                cv+=1

                                                    
                                                    
                        elif(m==2):
                            for i in range(46):
                                if('KAWASAKI' in bikename):
                                    for j in range(0,10):
                                        cm=allbike[j]
                                        if(variant[i]==cm):
                                            for k,l in KAWASAKI[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'KAWASAKI {cm} {k}',variable=vbr,value=cv)
                                                        variables6[f'svariantb{cv}'].grid(row=cv,column=0)
                                                        veriofb.append(k)
                                                        veriofbn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'KAWASAKI {cm} {k}',variable=vbr,value=cv)
                                                            variables6[f'svariantb{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofb.append(k)
                                                            veriofbn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'KAWASAKI {cm} {k}',variable=vbr,value=cv)
                                                                variables6[f'svariantb{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofb.append(k)
                                                                veriofbn.append(cm)
                                                                cv2+=1
                                                                cv+=1
                                                            else:
                                                                if(cv3<28):
                                                                    variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'KAWASAKI {cm} {k}',variable=vbr,value=cv)
                                                                    variables6[f'svariantb{cv}'].grid(row=cv3,column=6,padx=10)
                                                                    veriofb.append(k)
                                                                    veriofbn.append(cm)
                                                                    cv3+=1
                                                                    cv+=1


                                                    
                                                    
                                if('Honda' in bikename):
                                    for j in range(10,21):
                                        cm=allbike[j]
                                        if(variant[i]==cm):
                                            for k,l in Honda[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'Honda {cm} {k}',variable=vbr,value=cv)
                                                        variables6[f'svariantb{cv}'].grid(row=cv,column=0)
                                                        veriofb.append(k)
                                                        veriofbn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'Honda {cm} {k}',variable=vbr,value=cv)
                                                            variables6[f'svariantb{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofb.append(k)
                                                            veriofbn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'Honda {cm} {k}',variable=vbr,value=cv)
                                                                variables6[f'svariantb{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofb.append(k)
                                                                veriofbn.append(cm)
                                                                cv2+=1
                                                                cv+=1
                                                            else:
                                                                if(cv3<28):
                                                                    variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'Honda {cm} {k}',variable=vbr,value=cv)
                                                                    variables6[f'svariantb{cv}'].grid(row=cv3,column=6,padx=10)
                                                                    veriofb.append(k)
                                                                    veriofbn.append(cm)
                                                                    cv3+=1
                                                                    cv+=1

                                                    
                                                    
                                if('BAJAJ' in bikename):
                                    for j in range(21,31):
                                        cm=allbike[j]
                                        if(variant[i]==cm):
                                            for k,l in BAJAJ[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'BAJAJ {cm} {k}',variable=vbr,value=cv)
                                                        variables6[f'svariantb{cv}'].grid(row=cv,column=0)
                                                        veriofb.append(k)
                                                        veriofbn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'BAJAJ {cm} {k}',variable=vbr,value=cv)
                                                            variables6[f'svariantb{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofb.append(k)
                                                            veriofbn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'BAJAJ {cm} {k}',variable=vbr,value=cv)
                                                                variables6[f'svariantb{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofb.append(k)
                                                                veriofbn.append(cm)
                                                                cv2+=1
                                                                cv+=1
                                                            else:
                                                                if(cv3<28):
                                                                    variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'BAJAJ {cm} {k}',variable=vbr,value=cv)
                                                                    variables6[f'svariantb{cv}'].grid(row=cv3,column=6,padx=10)
                                                                    veriofb.append(k)
                                                                    veriofbn.append(cm)
                                                                    cv3+=1
                                                                    cv+=1

                                                    
                                                    
                                if('HERO' in bikename):
                                    for j in range(31,40):
                                        cm=allbike[j]
                                        if(variant[i]==cm):
                                            for k,l in HERO[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'HERO {cm} {k}',variable=vbr,value=cv)
                                                        variables6[f'svariantb{cv}'].grid(row=cv,column=0)
                                                        veriofb.append(k)
                                                        veriofbn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'HERO {cm} {k}',variable=vbr,value=cv)
                                                            variables6[f'svariantb{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofb.append(k)
                                                            veriofbn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'HERO {cm} {k}',variable=vbr,value=cv)
                                                                variables6[f'svariantb{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofb.append(k)
                                                                veriofbn.append(cm)
                                                                cv2+=1
                                                                cv+=1
                                                            else:
                                                                if(cv3<28):
                                                                    variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'HERO {cm} {k}',variable=vbr,value=cv)
                                                                    variables6[f'svariantb{cv}'].grid(row=cv3,column=6,padx=10)
                                                                    veriofb.append(k)
                                                                    veriofbn.append(cm)
                                                                    cv3+=1
                                                                    cv+=1

                                                    
                                                    
                                if('YAMAHA' in bikename):
                                    for j in range(40,46):
                                        cm=allbike[j]
                                        if(variant[i]==cm):
                                            for k,l in YAMAHA[cm]['Variants-price'].items():
                                                if(mk<l<mk1):
                                                    if(cv<28):

                                    
                                                        variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'YAMAHA {cm} {k}',variable=vbr,value=cv)
                                                        variables6[f'svariantb{cv}'].grid(row=cv,column=0)
                                                        veriofb.append(k)
                                                        veriofbn.append(cm)
                                                        cv+=1
                                                    else:
                                                        if(cv1<28): 
                                                            variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'YAMAHA {cm} {k}',variable=vbr,value=cv)
                                                            variables6[f'svariantb{cv}'].grid(row=cv1,column=2,padx=10)
                                                            veriofb.append(k)
                                                            veriofbn.append(cm)
                                                            cv1+=1
                                                            cv+=1
                                                        else:
                                                            if(cv2<28):
                                                                variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'YAMAHA {cm} {k}',variable=vbr,value=cv)
                                                                variables6[f'svariantb{cv}'].grid(row=cv2,column=4,padx=10)
                                                                veriofb.append(k)
                                                                veriofbn.append(cm)
                                                                cv2+=1
                                                                cv+=1
                                                            else:
                                                                if(cv3<28):
                                                                    variables6[f'svariantb{cv}']=Radiobutton(f2,text=f'YAMAHA {cm} {k}',variable=vbr,value=cv)
                                                                    variables6[f'svariantb{cv}'].grid(row=cv3,column=6,padx=10)
                                                                    veriofb.append(k)
                                                                    veriofbn.append(cm)
                                                                    cv3+=1
                                                                    cv+=1

                                                    
                                                    

                                
                        def back5():
                            t61.destroy()
                            f2.destroy()

                            cv=0
                            cv1=0
                            cv2=0
                            cv3=0
                            if(m==1):
                                for i in range(15):
                                    if('HONDA' in carname):
                                        for j in range(0,3):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in HONDA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                                                
                                    if('MAHINDRA' in carname):
                                        for j in range(3,6):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in MAHINDRA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                                                
                                    if('LAMBORGHINI' in carname):
                                        for j in range(6,9):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in LAMBORGHINI[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                                                
                                    if('TATA' in carname):
                                        for j in range(9,12):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in TATA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                
                                    if('PORSCHE' in carname):
                                        for j in range(12,15):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in PORSCHE[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                            elif(m==2):
                                for i in range(46):
                                    if('KAWASAKI' in bikename):
                                        for j in range(0,10):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in KAWASAKI[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1
                                                                

                                                        
                                                
                                    if('Honda' in bikename):
                                        for j in range(10,21):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in Honda[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1

                                                        
                                                
                                    if('BAJAJ' in bikename):
                                        for j in range(21,31):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in BAJAJ[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1

                                                        
                                                
                                    if('HERO' in bikename):
                                        for j in range(31,40):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in HERO[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1

                                                
                                    if('YAMAHA' in bikename):
                                        for j in range(40,46):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in YAMAHA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1

                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1

                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1


                                                        

                            b61.destroy()
                            b62.destroy()
                            tab5()                    


                                          
                        b61=Button(root,text='Back',bg='red',command=back5)
                        b61.grid(row=0,column=0,pady=00,padx=10)

                        def tab7():
                            t61.destroy()
                            f2.destroy()
                            cv=0
                            cv1=0
                            cv2=0
                            cv3=0
                            if(m==1):
                                for i in range(15):
                                    if('HONDA' in carname):
                                        for j in range(0,3):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in HONDA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                                                
                                    if('MAHINDRA' in carname):
                                        for j in range(3,6):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in MAHINDRA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                                                
                                    if('LAMBORGHINI' in carname):
                                        for j in range(6,9):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in LAMBORGHINI[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                                                
                                    if('TATA' in carname):
                                        for j in range(9,12):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in TATA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                                                
                                    if('PORSCHE' in carname):
                                        for j in range(12,15):
                                            cm=allcar[j]
                                            if(variant[i]==cm):
                                                for k,l in PORSCHE[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables3[f'svariant{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables3[f'svariant{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables3[f'svariant{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1

                                                        
                            elif(m==2):
                                for i in range(46):
                                    if('KAWASAKI' in bikename):
                                        for j in range(0,10):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in KAWASAKI[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1

                                                        
                                                
                                    if('Honda' in bikename):
                                        for j in range(10,21):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in Honda[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1

                                                        
                                                
                                    if('BAJAJ' in bikename):
                                        for j in range(21,31):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in BAJAJ[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1

                                                        
                                                
                                    if('HERO' in bikename):
                                        for j in range(31,40):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in HERO[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1
                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1
                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1
                   
                                    if('YAMAHA' in bikename):
                                        for j in range(40,46):
                                            cm=allbike[j]
                                            if(variant[i]==cm):
                                                for k,l in YAMAHA[cm]['Variants-price'].items():
                                                    if(mk<l<mk1):
                                                        if(cv<28):

                                    
                                                            variables6[f'svariantb{cv}'].destroy()
                                                            cv+=1

                                                        else:
                                                            if(cv1<28): 
                                                                variables6[f'svariantb{cv}'].destroy()
                                                                cv1+=1
                                                                cv+=1

                                                            else:
                                                                if(cv2<28):
                                                                    variables6[f'svariantb{cv}'].destroy()
                                                                    cv2+=1
                                                                    cv+=1
                                                                else:
                                                                    if(cv3<28):
                                                                        variables6[f'svariantb{cv}'].destroy()
                                                                        cv3+=1
                                                                        cv+=1

                            b61.destroy()
                            b62.destroy()
                            
                            

                            
                            variables7={}
                            if(m==1):
                                l71=Label(root,text='Car Detalis :',font='lucida 20 bold')
                                l71.grid(row=5,column=6,padx=630)
                            elif(m==2):
                                l71=Label(root,text='Bike Detalis :',font='lucida 20 bold')
                                l71.grid(row=5,column=6,padx=630)
                            l72=Label(root,text='',font='lucida 20 bold')
                            l72.grid(row=6,column=6,padx=630)
                            f3=Frame(root,borderwidth=20,relief=SUNKEN)
                            f3.grid(row=7,column=6)
                            lc=0
                            lc1=0
                            regisotr={}
                            getv=vbr.get()
                            # print('No :',getv)
                            # print('car variant :',len(veriofc))
                            # print('car name',len(veriofcn))
                            # print('bike variant :',len(veriofb))
                            # print('bike name',len(veriofbn))
                            # print(m)
                            if(m==1):
                                for i in range(len(veriofcn)):
                                    # print(i)
                                    # print(getv)
                                    if(getv==i):
                                        h=veriofc[i]
                                        c=veriofcn[i]
                                        # print(h)
                                        # print(c)
                                        
                                        for p in range(len(car)):
                                            for j in car[p].keys():
                                
                                                
                                                nh=car[p]
                                                for k,l in nh[j]['Variants-price'].items():
                                                    
                                                    if(mk<l<mk1):
                                                        if(c==j):
                                                            if(k==h): 
                                                                for b in nh[j].keys():
                                                                 
                                                                    if(b!='Variants-price'):
                                                                        po= nh[j][b]
                                                                        variables7[f'last{lc}']=Label(f3,text=f"{b} : {po}",font='lucida 10 bold')
                                                                        variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                        regisotr[b]=po
                                                                        lc+=1
                                                                        if(lc1==0):
                                                                            variables7[f'last{lc}']=Label(f3,text=f"Car Name : {j}",font='lucida 10 bold')
                                                                            variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                            regisotr['Car Name']=j
                                                                            lc+=1
                                                                        lc1+=1
                                                                    else:
                                                                        for g,hp in nh[j]['Variants-price'].items():
                                                                            if(g==h):
                                                                                # print(g,hp)
                                                                                variables7[f'last{lc}']=Label(f3,text=f"Variant Name : {g}",font='lucida 10 bold')
                                                                                variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                                regisotr['Variant Name']=g
                                                                                lc+=1
                                                                                variables7[f'last{lc}']=Label(f3,text=f"Price : {hp}",font='lucida 10 bold')
                                                                                variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                                regisotr['Price']=hp
                                                                    lc+=1
                            elif(m==2):
                                for i in range(len(veriofb)):
                                    # print(i)
                                    # print(getv)
                                    if(getv==i):
                                        h=veriofb[i]
                                        c=veriofbn[i]
                                        # print(h)
                                        # print(c)
                                        
                                        for p in range(len(bike)):
                                            for j in bike[p].keys():
                                
                                                
                                                nh=bike[p]
                                                for k,l in nh[j]['Variants-price'].items():
                                                    
                                                    if(mk<l<mk1):
                                                        if(c==j):
                                                            if(k==h): 
                                                                for b in nh[j].keys():
                                                                    if(b!='Variants-price'):
                                                                        po= nh[j][b]
                                                                        variables7[f'last{lc}']=Label(f3,text=f"{b} : {po}",font='lucida 10 bold')
                                                                        variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                        regisotr[b]=po
                                                                        lc+=1
                                                                        if(lc1==0):
                                                                            variables7[f'last{lc}']=Label(f3,text=f"Bike Name : {j}",font='lucida 10 bold')
                                                                            variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                            regisotr['Bike Name']=j
                                                                            lc+=1
                                                                        lc1+=1
                                                                    else:
                                                                        for g,hp in nh[j]['Variants-price'].items():
                                                                            if(g==h):
                                                                                print(g,hp)
                                                                                variables7[f'last{lc}']=Label(f3,text=f"Variant Name : {g}",font='lucida 10 bold')
                                                                                variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                                regisotr['Variant Name']=g
                                                                                lc+=1
                                                                                variables7[f'last{lc}']=Label(f3,text=f"Price : {hp}",font='lucida 10 bold')
                                                                                variables7[f'last{lc}'].grid(row=lc,column=0)
                                                                                regisotr['Price']=hp
                                                                    lc+=1
                            print(regisotr)
                            def back6():
                                l71.destroy()
                                l72.destroy()
                                f3.destroy()
                                lc=0
                                lc1=0
                                if(m==1):
                                    for i in range(len(veriofc)):
                                        if(getv==i):
                                            h=veriofc[i]
                                            c=veriofcn[i]
                                            for p in range(len(car)):
                                                for j in car[p].keys():
                                
                                                
                                                    nh=car[p]
                                                    for k,l in nh[j]['Variants-price'].items():
                                                        
                                                        if(mk<l<mk1):
                                                            if(c==j):
                                                                if(k==h): 
                                                                    for b in nh[j].keys():
                                                                 
                                                                        if(b!='Variants-price'):
                                                                            po= nh[j][b]
                                                                            variables7[f'last{lc}'].destroy()
                                                                            lc+=1
                                                                            if(lc1==0):
                                                                                variables7[f'last{lc}'].destroy()
                                                                                lc+=1
                                                                            lc1+=1
                                                                        else:
                                                                            for g,hp in nh[j]['Variants-price'].items():
                                                                                if(g==h):
                                                                                    # print(g,hp)
                                                                                    variables7[f'last{lc}'].destroy()
                                                                                    lc+=1
                                                                                    variables7[f'last{lc}'].destroy()
                                                                            
                                                                        lc+=1
                                elif(m==2):
                                    for i in range(len(veriofb)):
                                        if(getv==i):
                                            h=veriofb[i]
                                            c=veriofbn[i]
                                            for p in range(len(bike)):
                                                for j in bike[p].keys():
                                
                                                
                                                    nh=bike[p]
                                                    for k,l in nh[j]['Variants-price'].items():
                                                        
                                                        if(mk<l<mk1):
                                                            if(c==j):
                                                                if(k==h): 
                                                                    for b in nh[j].keys():
                                                                 
                                                                        if(b!='Variants-price'):
                                                                            po= nh[j][b]
                                                                            variables7[f'last{lc}'].destroy()
                                                                            lc+=1
                                                                            if(lc1==0):
                                                                                variables7[f'last{lc}'].destroy()
                                                                                lc+=1
                                                                            lc1+=1
                                                                        else:
                                                                            for g,hp in nh[j]['Variants-price'].items():
                                                                                if(g==h):
                                                                                    # print(g,hp)
                                                                                    variables7[f'last{lc}'].destroy()
                                                                                    lc+=1
                                                                                    variables7[f'last{lc}'].destroy()
                                                                            
                                                                        lc+=1

                                cb1.destroy()
                                l73.destroy()
                                cb2.destroy()
                                cb3.destroy()
                                tab6()

                            cb1=Button(root,text='Back',bg='red',command=back6)
                            cb1.grid(row=11,column=0,pady=350,padx=10)
                            l73=Label(root,text='',font='lucida 20 bold')
                            l73.grid(row=8,column=6,padx=650)
                            cb2=Button(root,text='Register',bg='green')
                            cb2.grid(row=9,column=6)
                            cb3=Button(root,text='Quit',bg='purple',command=quit)
                            cb3.grid(row=11,column=7,padx=0,pady=350)


                        b62=Button(root,text='Next',bg='green',command=tab7)
                        b62.grid(row=0,column=2,padx=0)

                    b52=Button(root,text='Next',bg='green',command=tab6)
                    b52.grid(row=11,column=7,padx=90)

                ba1=Button(root,text='Next',bg='green',command=tab5)
                ba1.grid(row=11,column=7,padx=90)
      
            b8=Button(root,text="Next",fg='black',bg='green',command=tab4,anchor='nw')
            b8.grid(row=9,column=60,pady=0,padx=130)
            
        b4=Button(root,text='Next',fg='black',bg='green',command=tab3,anchor='nw')
        b4.grid(row=9,column=60,pady=0,padx=30)


    ti=Label(root,text='Welcome To Car & Bike Info System',fg='black',font='lucida 40 bold',bg='yellow',padx=60,pady=20)
    ti.grid(row=2,column=5)
    global username
    username=StringVar()
    global password
    password=StringVar()
    global age
    age=IntVar()
    global mo
    mo=StringVar()

    l5=Label(root,text='')
    l5.grid(row=3)
    l6=Label(root,text='')
    l6.grid(row=4)
    l7=Label(root,text='')
    l7.grid(row=5)
    l8=Label(root,text='')
    l8.grid(row=6)
    l9=Label(root,text='')
    l9.grid(row=7)


    l1=Label(root,text='UserName',font="comicsansms 13 bold",padx=20)
    l1.grid(row=8,column=1)
    l2=Label(root,text='Password',font="comicsansms 13 bold")
    l2.grid(row=9,column=1)
    l3=Label(root,text='age',font="comicsansms 13 bold")
    l3.grid(row=10,column=1)
    l4=Label(root,text='Phone No.',font="comicsansms 13 bold")
    l4.grid(row=11,column=1)

    userentry=Entry(root,textvariable=username)
    userentry.grid(row=8,column=2)
    passentry=Entry(root,textvariable=password)
    passentry.grid(row=9,column=2)
    ageentry=Entry(root,textvariable=age)
    ageentry.grid(row=10,column=2)
    moentry=Entry(root,textvariable=mo)
    moentry.grid(row=11,column=2)
    l10=Label(root,text='')
    l10.grid(row=12,column=2)
    b1=Button(root,text='Submit',fg='black',bg='green',command=getval)
    b1.grid(row=13,column=2)
    b2=Button(root,text='Next >>',fg='black',bg='green',anchor='ne',command=tab2)
    b2.grid(row=15,column=15,pady=400,padx=180)

tab1()
root.mainloop()