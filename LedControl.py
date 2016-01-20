import RPi.GPIO as GPIO
import time
import easygui
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
HowManyLed = int(input("რამდენი ნათურა გაქვთ?\t"))
LedsNumber = []
for LedsNumberLoop in range (HowManyLed):
    LedsNumber.append(LedsNumberLoop + 1)
print(LedsNumber)
Leds = []
for LedsLoop in range(1, HowManyLed + 1):
    LedsInput = int(input("ჩაწერეთ %s ნათურის პინის ნომერი:\t" % LedsNumber[LedsLoop - 1]))
    Leds.append(LedsInput)
    GPIO.setup(Leds[LedsLoop - 1],GPIO.OUT)
print(Leds)
i = 1
while i == 1:
    for MenuLoop in range(HowManyLed):
        MenuList = ["LED ნათება\n","1080.მეტი\n1090.გამოსვლა\nშეიყვანე ციფრი:\t"]
        MenuListIndex = 1
        MenuListLedNumber = 1
        MenuListNumberOne = 1
        MenuListNumberTwo = 2
        MenuListNumberThree = 3

        strMenuListLedNumber = str(MenuListLedNumber)
        strMenuListNumberOne = str(MenuListNumberOne)
        strMenuListNumberTwo = str(MenuListNumberTwo)
        strMenuListNumberThree = str(MenuListNumberThree)

        MenuListString = strMenuListNumberOne,". ",strMenuListLedNumber," ნათურა - ჩართვა\n",strMenuListNumberTwo,". ",strMenuListLedNumber," ნათურა - ციმციმი\n",strMenuListNumberThree,". ",strMenuListLedNumber," ნათურა - გამორთვა\n"
        MenuList.insert(MenuListIndex, MenuListString)
        MenuListLedNumber += 1
        MenuListIndex += 1
        MenuListNumberOne += 3
        MenuListNumberTwo += 3
        MenuListNumberThree += 3
    MenuList = ''.join(str(e) for e in MenuList)
    reply = int(input(MenuList))
    print("\n")
## First Led

#### First Led ჩართვა
    if reply == 1:
        GPIO.output(Leds[0],GPIO.HIGH)
        print("ნათურა აინთო")
#### First Led ციმციმი
    elif reply == 2:
        redblink = True
        while redblink == True:
            print("\nციმციმი")
            replyredblink = int(input("1.უხეში ციმციმი\n2.ნაზი ციმციმი\n3.ციმციმის გამორთვა\n"))
            if replyredblink == 1:
                BlinkNumberRed = int(input("რამდენჯერ უნდა დაიციმციმოს?\t"))
                BlinkPerSecondRed = float(input("რა სიჩქარით იციმციმოს? x დაციმციმება 1 წამში\t"))
                timesleepred = 1 / BlinkPerSecondRed
                for x in range(BlinkNumberRed):
                    GPIO.output(Leds[0],GPIO.HIGH)
                    time.sleep(timesleepred)
                    GPIO.output(Leds[0],GPIO.LOW)
                    time.sleep(timesleepred)
            else:
                redblink = False
#### First Led გამორთვა
    elif reply == 3:
        GPIO.output(Leds[0],GPIO.LOW)

## მწვანე
    elif reply == "მწვანე-ჩართვა":
        GPIO.output(greenledpin,GPIO.HIGH)
    elif reply == "მწვანე-ციმციმი":
        greenblink = True
        while greenblink == True:
            replygreenblink = easygui.buttonbox("ციმციმი",choices = ["ციმციმი","ციმციმის გამორთვა"])
            if replygreenblink == "ციმციმი":
                blinknumbergreen = easygui.integerbox("რამდენჯერ უნდა დაიციმციმოს?")
                blinkpersecondgreen = easygui.integerbox("რა სიჩქარით იციმციმოს? x დაციმციმება 1 წამში  ")
                timesleepgreen = 1 / blinkpersecondgreen
                for x in range(blinknumbergreen):
                    GPIO.output(greenledpin,GPIO.HIGH)
                    time.sleep(timesleepgreen)
                    GPIO.output(greenledpin,GPIO.LOW)
                    time.sleep(timesleepgreen)
            elif replygreenblink == "ციმციმის გამორთვა":
                greenblink = False
    elif reply == "მწვანე-გამორთვა":
        GPIO.output(greenledpin,GPIO.LOW)

## მენიუ მეტი
    elif reply == 1080:
        meti = True
        while meti == True:
            metimenu = easygui.buttonbox("დააჭირეთ ღილაკს",choices = ["ნათურის სიკაშკაშე","შემთხვევითი ნათება","მასიური ციმციმი","გამოსვლა"])

        ## ნათურის სიკაშკაშე
            if metimenu == "ნათურის სიკაშკაშე":

            ## ნათურის არჩევა სიკაშკაშე
                ledbrightnessledchoiceloop = True
                while ledbrightnessledchoiceloop == True:
                    ledchoicebrightness = easygui.buttonbox("აირჩიეთ ნათურა",choices = ["First Led","მწვანე","თეთრი","გამოსვლა"])

                    ## First Led ნათურის სიკაშკაშე
                    if ledchoicebrightness == "First Led":
                        redledbrightnessloop = True
                        while redledbrightnessloop == True:
                            ledbrightnesswelcome = easygui.indexbox("First Led ნათურის სიკაშკაშის კონტროლი\nგსურთ გაგრძელება?",choices = ["დიახ","არა"])
                            if ledbrightnesswelcome == 0:
                                redledbrightnessdutycycle = easygui.integerbox("Duty cycle",default = 50,lowerbound = 0,upperbound = 100) # change later
                                redbrightness = GPIO.PWM(Leds[0], 200)
                                redbrightness.start(redledbrightnessdutycycle)
                            else:
                                redbrightness.stop()
                                ledbrightnessloop = False
                                ledbrightnessledchoiceloop = False
                    if ledchoicebrightness == "მწვანე":
                        greenledbrightnessloop = True
                        while greenledbrightnessloop == True:
                            greenledbrightnesswelcome = easygui.indexbox("მწვანე ნათურის სიკაშკაშის კონტროლი\nგსურთ გაგრძელება?",choices = ["დიახ","არა"])
                            if greenledbrightnesswelcome == 0:
                                greenledbrightnessdutycycle = easygui.integerbox("აირჩიეთ სიკაშკაშის დონე\n0 - min // 100 - max",default = 50,lowerbound = 0,upperbound = 100) # change later
                                greenbrightness = GPIO.PWM(greenledpin,200)
                                greenbrightness.start(greenledbrightnessdutycycle)
                            else:
                                greenbrightness.stop()
                                greenledbrightnessloop = False
                                GPIO.cleanup()
                    else:
                        ledbrightnessledchoiceloop = False
                        GPIO.cleanup()

            ## შემთხვევითი ნათება
            elif metimenu == "შემთხვევითი ნათება (მასიური)":
                pass

            ## მასიური ციმციმი
            elif metimenu == "მასიური ციმციმი":
                randomblinkloop = True
                while randomblinkloop == True:
                    welcomerandomblinkloop = easygui.buttonbox("გსურთ გაგრძელება?", choices =  ["კი","არა"])
                    if welcomerandomblinkloop == "კი":
                        numberofrandomblink = easygui.integerbox("რაოდენობა: ",default = 5,lowerbound = 0,upperbound = 50)
                        speedofrandomblinkstring = easygui.enterbox("სიჩქარე")
                        speedofrandomblinkfloat = float(speedofrandomblinkstring)
                        for randomblinkforloop in range(numberofrandomblink):

                            GPIO.output(Leds[0],GPIO.HIGH) #red
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(Leds[0],GPIO.LOW)

                            GPIO.output(whiteledpin,GPIO.HIGH) #white
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(whiteledpin,GPIO.LOW)

                            GPIO.output(greenledpin,GPIO.HIGH) #green
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(greenledpin,GPIO.LOW)

                            GPIO.output(blueledpin,GPIO.HIGH) #blueledpin
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(blueledpin,GPIO.LOW)
                    else:
                        randomblinkloop == False

        ## მენიუ მეტიდან გამოსვლა
            else:
                meti = False

    ## გამოსვლა
    else:
        exit = easygui.buttonbox("ნამდვიალად გსურთ გამოსვლა?",choices=["კი","არა"])
        if exit == ("კი"):
            i=2
            GPIO.cleanup()
        else:
            print("-")
            pass
