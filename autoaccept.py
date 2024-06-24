import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch, imagesearch_region_loop
import time

pyautogui.FAILSAFE = False
TIMELAPSE = 2

acceptButtonImg = 'sample.png'
acceptedButtonImg = 'accepted.png'
championSelectionImg_flash = 'flash-icon.png'
championSelectionImg_emote = 'emote-icon.png'
playButtonImg = 'play-button.png'
inqueue = 'inqueue.png'

def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            print(pos[0], pos[1])
            print("Game acceptée!")
            break
        
        
    

def checkChampionSelection():
    flash = imagesearch(championSelectionImg_flash)
    emote = imagesearch(championSelectionImg_emote)

    if not emote[0] == -1 or not flash[0] == -1:
        return True
    else:
        return False

def checkGameCancelled():
    accepted = imagesearch(acceptedButtonImg)
    play = imagesearch(playButtonImg)

    if accepted[0] == -1 and not play[0] == -1:
        return True
    else:
        return False


def main():
    
   
    q = imagesearch_loop(inqueue, 1)
    if not q[0] == -1:
        print("Recherche en cours...")
    else:
        print('ptnzebi')
    run = True

    while run is True:
        checkGameAvailableLoop()
        time.sleep(TIMELAPSE)

        while True:
            cancelled = checkGameCancelled()
            if cancelled is True:
                print("ça a dodge zebi...")
                main()
            time.sleep(TIMELAPSE)
            csResult = checkChampionSelection()
            if csResult is True:
                print("ça part, j'espère tu te fais int.")
                time.sleep(TIMELAPSE)
                run = False
                main()  

            time.sleep(TIMELAPSE)
                  
main()
    