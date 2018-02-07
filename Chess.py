from SimpleGraphics import *
from matplotlib.pyplot import ion,show
from matplotlib import pyplot as plt
from Tkinter import *
from math import sqrt
from random import randint
from datetime import datetime

def mapping(p):
    '''Position is a string. Converts position to x-y coordinates.
    Returns a list containing x and y coordinates.'''
    p=str(p)
    l=[]
    if p[0].upper()=='A':
        l.append(-7)
    elif p[0].upper()=='B':
        l.append(-5)
    elif p[0].upper()=='C':
        l.append(-3)
    elif p[0].upper()=='D':
        l.append(-1)
    elif p[0].upper()=='E':
        l.append(1)
    elif p[0].upper()=='F':
        l.append(3)
    elif p[0].upper()=='G':
        l.append(5)
    elif p[0].upper()=='H':
        l.append(7)
    l.append(-9+2*int(p[1]))
    return l

def reversemap(L):
    """takes a list, containing x and y coordinates representing a point
    and returns an alpha-numeric grid coordinate"""
    alpha='ABCDEFGH'
    l=alpha[int(L[0])+4]
    b=int(L[1])+5
    l=l+str(b)
    return l
    
####
# Directions for drawing game pieces
####
   
def DrawPawn(p,color):
    '''color is a boolean value. True for white, False for black'''
    if p=='None':
        pass
    else:
        if color:
            c=WHITE
        else:
            c=BLACK
        l=mapping(p)
        x=l[0]
        y=l[1]
        #MakeWindow(1,bgcolor=BLACK,labels=False)
        DrawRect(0+x,-.6+y,1.2,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,-.4+y,1,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,0+y,.5,.7,FillColor=c,EdgeColor=c)
        DrawDisk(0+x,.3+y,.35,FillColor=c,EdgeColor=c)
        #ShowWindow()
    
def DrawRook(p,color):
    '''color is a boolean value. True for white, False for black'''
    if p=='None':
        pass
    else:
        if color:
            c=WHITE
        else:
            c=BLACK
        l=mapping(p)
        x=l[0]
        y=l[1]
        #MakeWindow(1,bgcolor=BLACK,labels=False)
        DrawRect(0+x,-.6+y,1.2,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,-.4+y,1,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,0+y,.5,.7,FillColor=c,EdgeColor=c)
        DrawRect(0+x,.2+y,.8,.4,FillColor=c,EdgeColor=c)
        for i in range(4):
            DrawRect(-.4*(6.0/7)+1.6/7*i+x,.45+y,.8/7,.15,FillColor=c,EdgeColor=c)
        #ShowWindow()
    
def DrawBishop(p,color):
    '''color is a boolean value. True for white, False for black'''
    if p=='None':
        pass
    else:
        if color:
            c=WHITE
        else:
            c=BLACK
        l=mapping(p)
        x=l[0]
        y=l[1]
        #MakeWindow(1,bgcolor=BLACK,labels=False)
        DrawRect(0+x,-.6+y,1.2,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,-.4+y,1,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,0+y,.5,.8,FillColor=c,EdgeColor=c)
        DrawDisk(0+x,.3+y,.35,FillColor=c,EdgeColor=c)
        DrawPoly([-.315+x,0+x,.315+x],[.45+y,.85+y,.45+y],FillColor=c,EdgeColor=c)
        DrawRect(0+x,0+y,.65,.1,FillColor=c,EdgeColor=c)
        #ShowWindow()
    
def DrawQueen(p,color):
    '''color is a boolean value. True for white, False for black'''
    if p=='None':
        pass
    else:
        if color:
            c=WHITE
        else:
            c=BLACK
        l=mapping(p)
        x=l[0]
        y=l[1]
        #MakeWindow(1,bgcolor=BLACK,labels=False)
        DrawRect(0+x,-.6+y,1.2,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,-.4+y,1,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,0+y,.5,.8,FillColor=c,EdgeColor=c)
        DrawRect(0+x,.1+y,.65,.15,FillColor=c,EdgeColor=c)
        DrawPoly([-.3+x,-.2+x,.2+x,.3+x],[.3+y,.5+y,.5+y,.3+y],FillColor=c,EdgeColor=c)
        DrawPoly([-.2+x,-.3+x,0+x,.3+x,.2+x],[.5+y,.7+y,.75+y,.7+y,.5+y],FillColor=c,EdgeColor=c)
        DrawDisk(0+x,.75+y,.07,FillColor=c,EdgeColor=c)
        #ShowWindow()
    
def DrawKing(p,color):
    '''color is a boolean value. True for white, False for black'''
    if p=='None':
        pass
    else:
        if color:
            c=WHITE
        else:
            c=BLACK
        l=mapping(p)
        x=l[0]
        y=l[1]
        #MakeWindow(1,bgcolor=BLACK,labels=False)
        DrawRect(0+x,-.6+y,1.2,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,-.4+y,1,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,0+y,.5,.8,FillColor=c,EdgeColor=c)
        DrawRect(0+x,.1+y,.65,.15,FillColor=c,EdgeColor=c)
        DrawPoly([-.3+x,-.2+x,.2+x,.3+x],[.3+y,.5+y,.5+y,.3+y],FillColor=c,EdgeColor=c)
        DrawPoly([-.2+x,-.3+x,0+x,.3+x,.2+x],[.5+y,.7+y,.75+y,.7+y,.5+y],FillColor=c,EdgeColor=c)
        DrawRect(0+x,.75+y,.07,.3,FillColor=c,EdgeColor=c)
        DrawRect(0+x,.82+y,.2,.06,FillColor=c,EdgeColor=c)
        #ShowWindow()
       
def DrawKnight(p,color):
    '''color is a boolean value. True for white, False for black'''
    if p=='None':
        pass
    else:
        if color:
            c=WHITE
        else:
            c=BLACK
        l=mapping(p)
        x=l[0]
        y=l[1]
        #MakeWindow(1,bgcolor=BLACK,labels=True)
        DrawRect(0+x,-.6+y,1.2,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,-.4+y,1,.2,FillColor=c,EdgeColor=c)
        DrawRect(0+x,0+y,.5,.7,FillColor=c,EdgeColor=c)
        DrawPoly([0+x,.2+x,.4+x,.3+x,.07+x,-.23+x,-.46+x,-.58+x,-.73+x,-.6+x,-.4+x],[.3+y,-.2+y,.1+y,.5+y,.65+y,.65+y,.57+y,.3+y,0+y,-0.06+y,.015+y],FillColor=c,EdgeColor=c)
        DrawPoly([-.36+x,-.33+x,-.09+x],[.57+y,.75+y,.58+y],FillColor=c,EdgeColor=c)
        #ShowWindow()

####
# Restrictions on moves
####

def DetPiece(x):
    """Takes the starting location of the piece to be moved
    and returns a tuple that contains the name of the piece at
    that location and the boolean value of the color. Returns
    'None' if there is nothing located at the given position"""
    x=x[0].upper() + x[1]
    a=0
    for i in wpawn:
        if x==i:
            if wpromote[a]==None:
                return 'Pawn', True
            else:
                return wpromote[a], True
        a+=1
    
    b=0
    for j in bpawn:
        if x==j:
            if bpromote[b]==None:
                return 'Pawn', False
            else:
                return bpromote[b], False
        b+=1
        
    L=['Rook','Knight','Bishop','Queen','King','Bishop','Knight','Rook']
    for k in range(8):
        if wother[k]==x:
            return L[k], True
        if bother[k]==x:
            return L[k], False
    return None

def AlphaToNum(x):
    """Takes a letter representing the horiontal location on the grid
    and changes it to a number. Returns an int"""
    s='ABCDEFGH'
    n=0
    for i in s:
        n+=1
        if x==i:
            return n

def NumToAlpha(x):
    """Takes a number and returns the corresponding horizontal letter location"""
    s='ABCDEFGH'
    return s[x-1]

def PawnMove(color,start,end):
    """Determines whether a certain move is legal for a pawn to make.
    Takes a boolean value color and the alphanumeric values of
    the start and end locations and returns a boolean for legality."""
    start1=start[0]
    start2=start[1]
    end1=end[0]
    end2=end[1]
    if color==True:
        if end2<=start2:
            return False
    else:
        if end2>=start2:
            return False
    if DetPiece(end)==None:
        TakePiece = False
        try:
            global passant
            if color:
                a=AlphaToNum(end[0])
                if bpassant[a-1]==k-1 and int(end[1])-1==int(bpawn[a-1][1]):
                    TakePiece = True
                    passant = True
            else:
                a=AlphaToNum(end[0])
                if wpassant[a-1]==k-1 and int(end[1])+1==int(wpawn[a-1][1]):
                    TakePiece = True
                    passant = True
        except:
            pass
            
    elif DetPiece(end)[1]==(not color):
        TakePiece = True
    else:
        return False
        TakePiece = False
    if color:
        val='2'
    else:
        val='7'
    if start2 != val:
        if abs(int(end2)-int(start2))>1:
            return False
        if DetPiece(end)!=None and start1==end1:
            return False
        if TakePiece==False:
            if start1!=end1:
                return False
        else:
            if abs(AlphaToNum(start1)-AlphaToNum(end1))!=1:
                return False
    else:
        if abs(int(end2)-int(start2))>2:
            return False
        elif abs(int(end2)-int(start2))==2:
            if color:
                a=end1+str(int(end2)-1)
            else:
                a=end1+str(int(end2)+1)
            if DetPiece(a) != None:
                return False
            if DetPiece(end)!=None:
                return False
        elif abs(int(end2)-int(start2))==1:
            if (not TakePiece):
                if start1!=end1:
                    return False
            if TakePiece:
                a=AlphaToNum(end1)
                b=AlphaToNum(start1)
                if abs(b-a)!=1:
                    return False
        if (not TakePiece):
            if start1!=end1:
                return False
        #part that initializes en passant turn
        if color:
            wpassant[AlphaToNum(start[0])-1]=k
        else:
            bpassant[AlphaToNum(start[0])-1]=k
            
    return True

def RookMove(color,start,end):
    """Determines whether a certain move is legal for a rook to make.
    Takes a boolean value color and the alphanumeric values of
    the start and end locations and returns a boolean for legality."""
    start1=AlphaToNum(start[0])
    start2=int(start[1])
    end1=AlphaToNum(end[0])
    end2=int(end[1])
    a = (start1==end1 or start2==end2)
    if not a:
        return False
    if start1==end1:
        if start2<end2:
            for i in range(start2+1,end2):
                if DetPiece(start[0]+str(i))!=None:
                    return False
        if start2>end2:
            for i in range(end2+1,start2):
                if DetPiece(start[0]+str(i))!=None:
                    return False
    else:
        s="_ABCDEFGH"
        if start1<end1:
            for i in range(start1+1,end1):
                if DetPiece(s[i]+str(start2))!=None:
                    return False
        if start1>end1:
            for i in range(end1+1,start1):
                if DetPiece(s[i]+str(start2))!=None:
                    return False
    if DetPiece(end)!=None:
        if DetPiece(end)[1] == color:
            return False
    return True
    
def BishopMove(color,start,end):
    """Determines whether a certain move is legal for a bishop to make.
    Takes a boolean value color and the alphanumeric values of the
    start and end locations and returns a boolean for legality."""
    start1=AlphaToNum(start[0])
    start2=int(start[1])
    end1=AlphaToNum(end[0])
    end2=int(end[1])
    if abs(end2-start2)!=abs(end1-start1):
        return False
    if DetPiece(end)!=None:
        if DetPiece(end)[1]==color:
            return False
    L1=[]
    L2=[]
    if end1>start1:
        for i in range(start1+1,end1):
            L1.append(i)
    else:
        for i in range(end1+1,start1):
            L1.insert(0,i)
    if end2>start2:
        for i in range(start2+1,end2):
            L2.append(i)
    else:
        for i in range(end2+1,start2):
            L2.insert(0,i)
    s='_ABCDEFGH'
    for i in range(len(L1)):
        a=s[L1[i]]+str(L2[i])
        if DetPiece(a)!=None:
            return False
    return True
        
def QueenMove(color,start,end):
    """Determines whether a certain move is legal for a queen to make.
    Takes a boolean value color and the alphanumeric values of the
    start and end locations and returns a boolean for legality."""
    return (RookMove(color,start,end) or BishopMove(color,start,end))

def KingMove(color,start,end):
    """Determines whether a certain move is legal for a king to make.
    Takes a boolean value color and the alphanumeric values of the
    start and end locations and returns a boolean for legality."""
    start1=AlphaToNum(start[0])
    start2=int(start[1])
    end1=AlphaToNum(end[0])
    end2=int(end[1])
    dist=sqrt((start1-end1)**2+(start2-end2)**2)
    a=(dist<1.5)
    return (QueenMove(color,start,end) and a)

def KnightMove(color,start,end):
    """Determines whether a certain move is legal for a knight to make.
    Takes a boolean value color and the alphanumeric values of the
    start and end locations and returns a boolean for legality."""
    start1=AlphaToNum(start[0])
    start2=int(start[1])
    end1=AlphaToNum(end[0])
    end2=int(end[1])
    dist=sqrt((start1-end1)**2+(start2-end2)**2)
    if dist!=sqrt(5):
        return False
    if DetPiece(end)!=None:
        if DetPiece(end)[1]==color:
            return False
    return True

def Castle(color,start,end):
    start1=AlphaToNum(start[0])
    start2=int(start[1])
    end1=AlphaToNum(end[0])
    end2=int(end[1])
    other=False
    if color:
        k=b2
        if w2:
            return False
    else:
        k=w2
        if b2:
            return False
    if color:
        if end==wother[0]:
            other=w1
            if k:
                if InDanger(color,'E1') or InDanger(color,'C1') or InDanger(color,'D1'):
                    return False
            else:
                if InDanger(color,'E1',False) or InDanger(color,'C1',False) or InDanger(color,'D1',False):
                    return False
            if DetPiece('B1')!=None or DetPiece('C1')!=None or DetPiece('D1')!=None:
                return False
        elif end==wother[7]:
            other=w3
            if k:
                if InDanger(color,'E1') or InDanger(color,'F1') or InDanger(color,'G1'):
                    return False
            else:
                if InDanger(color,'E1',False) or InDanger(color,'F1',False) or InDanger(color,'G1',False):
                    return False
            if DetPiece('F1')!=None or DetPiece('G1')!=None:
                return False
    else:
        if end==bother[0]:
            other=b1
            if k:
                if InDanger(color,'E8') or InDanger(color,'C8') or InDanger(color,'D8'):
                    return False
            else:
                if InDanger(color,'E8',False) or InDanger(color,'C8',False) or InDanger(color,'D8',False):
                    return False
            if DetPiece('B8')!=None or DetPiece('C8')!=None or DetPiece('D8')!=None:
                return False
        elif end==bother[7]:
            other=b3
            if k:
                if InDanger(color,'E8') or InDanger(color,'F8') or InDanger(color,'G8'):
                    return False
            else:
                if InDanger(color,'E8',False) or InDanger(color,'F8',False) or InDanger(color,'G8',False):
                    return False
            if DetPiece('F8')!=None or DetPiece('G8')!=None:
                return False
    if other:
        return False
    return True

def InDanger(color,start,king=True,multiple=False):
    """determines if the opponent can attack a given square next turn.
    Returns a boolean value denoting ability to be attacked."""
    if color==True:
        l1=bpawn
        l2=bother
    else:
        l1=wpawn
        l2=wother
    multlist=[]
    moves=[]
    if king==True:
        for i in range(8):
            #makes sure that forward pawn moves are not deemed attacking locations
            L=Possible(l1[i])
            if DetPiece(l1[i])!=None:
                if DetPiece(l1[i])[0]=='Pawn':
                    for j in L:
                        if j[0]!=l1[i][0]:
                            moves.append(j)
                            if multiple:
                                if start==j:
                                    multlist.append(l1[i])
                else:
                    moves.extend(Possible(l1[i]))
            beta=Possible(l2[i])
            moves.extend(beta)
            if multiple:
                if start in beta:
                    multlist.append(l2[i])
    else:
        for i in range(8):
            L=Possible(l1[i])
            for j in L:
                if j[0]!=l1[i][0]:
                    moves.append(j)
        for i in range(4):
            moves.extend(Possible(l2[i]))
        for i in range(5,8):
            moves.extend(Possible(l2[i]))
    
    if start in moves:
        if multiple:
            return True, multlist
        return True
    else:
        if multiple:
            return False, []
        return False

def Possible(start):
    """Takes in a location and gives all locations that that piece can move to.
    Returns a list."""
    s='ABCDEFGH'
    L=[]
    global passant
    global castlebool
    passtemp = passant
    castletemp = castlebool
    if start=='None':
        return []
    piece=DetPiece(start)
    if piece[0]=='Pawn':
        for i in GetPawnMoves(piece[1],start):
            legal=PawnMove(piece[1],start,i)
            if legal:
                L.append(i)
    elif piece[0]=='Knight':
        for i in GetKnightMoves(piece[1],start):
            legal=KnightMove(piece[1],start,i)
            if legal:
                L.append(i)
    elif piece[0]=='Rook':
        for i in GetRookMoves(piece[1],start):
            legal=RookMove(piece[1],start,i)
            if legal:
                L.append(i)
    elif piece[0]=='Bishop':
        for i in GetBishopMoves(piece[1],start):
            legal=BishopMove(piece[1],start,i)
            if legal:
                L.append(i)
    elif piece[0]=='Queen':
        for i in GetQueenMoves(piece[1],start):
            legal=QueenMove(piece[1],start,i)
            if legal:
                L.append(i)
    elif piece[0]=='King':
        for i in GetKingMoves(piece[1],start):
            legal=KingMove(piece[1],start,i)
            #code to add castling to possible list
            if DetPiece(i)!=None:
                if piece[0]=='King' and DetPiece(i)[0]=='Rook' and piece[1]==DetPiece(i)[1]:
                    legal=Castle(piece[1],start,i)
            if legal:
                L.append(i)
    castlebool = castletemp
    passant = passtemp
    return L

def Check(color):
    """Determines if the king is in check"""
    if color:
        p=wother[4]
    else:
        p=bother[4]
    return InDanger(color,p)

def CheckMate(color):
    """Checks if a given color is in checkmate"""
    global passant
    global castlebool
    passbool=passant
    castletemp=castlebool
    for i in range(16):
        if color:
            L=[]
            L.extend(wpawn)
            L.extend(wother)
        else:
            L=[]
            L.extend(bpawn)
            L.extend(bother)
        poss=Possible(L[i])
        temp = L[i]
        if len(poss)>0:
            for j in poss:
                if i<8:
                    if color:
                        l=wpawn
                    else:
                        l=bpawn
                elif i>=8:
                    if color:
                        l=wother
                    else:
                        l=bother
                
                #checks if the move is a passant move
                passant = False
                if DetPiece(j)==None and DetPiece(l[i%8])[0]=='Pawn':
                    try:
                        if color:
                            a=AlphaToNum(j[0])
                            if bpassant[a-1]==k-1 and int(j[1])-1==int(bpawn[a-1][1]):
                                passant = True
                        else:
                            a=AlphaToNum(j[0])
                            if wpassant[a-1]==k-1 and int(j[1])+1==int(wpawn[a-1][1]):
                                passant = True
                    except:
                        pass
                    
                l[i%8]=j
                ltake=None
                if color:
                    for k in range(8):
                        if j==bpawn[k]:
                            bpawn[k]='None'
                            ltake=bpawn
                            c=k
                        elif j == bother[k]:
                            bother[k]='None'
                            ltake=bother
                            c=k
                    if passant==True:
                        a=AlphaToNum(j[0])-1
                        bpawn[a]='None'
                        ltake=bpawn
                        c=a
                else:
                    for k in range(8):
                        if j==wpawn[k]:
                            wpawn[k]='None'
                            ltake=wpawn
                            c=k
                        elif j == wother[k]:
                            wother[k]='None'
                            ltake=wother
                            c=k
                    if passant==True:
                        a=AlphaToNum(j[0])-1
                        wpawn[a]='None'
                        ltake=wpawn
                        c=a
                if Check(color)==False:
                    l[i%8]=temp
                    if ltake!=None:
                        ltake[c]=j
                    castlebool=castletemp
                    passant=passbool
                    return False
                l[i%8]=temp
                if ltake!=None:
                    ltake[c]=j
    castlebool=castletemp
    passant=passbool
    return True

def GetPawnMoves(color,start):
    """Takes in a start position and determines the locations
    that 'Possible' should look for legal moves"""
    x=AlphaToNum(start[0])
    y=int(start[1])
    if color:
        n=2
    else:
        n=1
    L=[[x+1,y+1*(-1)**n],[x-1,y+1*(-1)**n],[x,y+1*(-1)**n],[x,y+2*(-1)**n]]
    moves=[]
    for i in L:
        if i[0]<9 and i[0]>0 and i[1]<9 and i[1]>0:
            a=NumToAlpha(i[0])+str(i[1])
            moves.append(a)
    return moves
    
def GetKnightMoves(color,start):
    """Takes in a start position and determines the locations
    that 'Possible' should look for legal moves"""
    x=AlphaToNum(start[0])
    y=int(start[1])
    L=[[x-2,y+1],[x-2,y-1],[x-1,y+2],[x-1,y-2],[x+1,y+2],[x+1,y-2],[x+2,y+1],[x+2,y-1]]
    moves=[]
    for i in L:
        if i[0]<9 and i[0]>0 and i[1]<9 and i[1]>0:
            a=NumToAlpha(i[0])+str(i[1])
            moves.append(a)
    return moves

def GetRookMoves(color,start):
    """Takes in a start position and determines the locations
    that 'Possible' should look for legal moves"""
    x=AlphaToNum(start[0])
    y=int(start[1])
    L=[]
    for i in range(1,9):
        L.append([x,i])
        L.append([i,y])
    moves=[]
    for i in L:
        if i[0]<9 and i[0]>0 and i[1]<9 and i[1]>0:
            a=NumToAlpha(i[0])+str(i[1])
            moves.append(a)
    return moves

def GetBishopMoves(color,start):
    """Takes in a start position and determines the locations
    that 'Possible' should look for legal moves"""
    x=AlphaToNum(start[0])
    y=int(start[1])
    L=[]
    for i in range(1,8):
        L.append([x+i,y+i])
        L.append([x-i,y+i])
        L.append([x+i,y-i])
        L.append([x-i,y-i])
    moves=[]
    for i in L:
        if i[0]<9 and i[0]>0 and i[1]<9 and i[1]>0:
            a=NumToAlpha(i[0])+str(i[1])
            moves.append(a)
    return moves

def GetQueenMoves(color,start):
    """Takes in a start position and determines the locations
    that 'Possible' should look for legal moves"""
    moves=[]
    moves.extend(GetBishopMoves(color,start))
    moves.extend(GetRookMoves(color,start))
    return moves

def GetKingMoves(color,start):
    """Takes in a start position and determines the locations
    that 'Possible' should look for legal moves"""
    x=AlphaToNum(start[0])
    y=int(start[1])
    if color:
        moves=['A1','H1']
    else:
        moves=['A8','H8']
    L=[[x,y+1],[x,y-1],[x+1,y],[x-1,y],[x+1,y+1],[x+1,y-1],[x-1,y+1],[x-1,y-1]]
    for i in L:
        if i[0]<9 and i[0]>0 and i[1]<9 and i[1]>0:
            a=NumToAlpha(i[0])+str(i[1])
            moves.append(a)
    return moves

####
# Code for the AI
####

value = {'Pawn':1,'Knight':3,'Bishop':3.5,'Rook':5,'Queen':9,'King':516}

def Strength(color,wpn,woth,bpn,both,wpro,bpro,Danger=True,cCheck=False):
    """Determines the strength of the board for a color. Takes
    in the board settings and a color and returns a value that
    denotes how strong the board position is.
    
    The color is the color of the move that is being checked for the AI.
    
    cCheck is a boolean value that determines whether to count whether a king is in check
    against the strength total."""
    global passant
    global castlebool
    passant=False
    castlebool=False
    global value
    spaces=['C6','C3','D4','D5','E4','E5','F6','F3']
    val=0
    wdanger=[0,0]
    bdanger=[0,0]
    for i in range(8):
        if wpn[i]!='None':
            gamma=wpn[i][1]
            if gamma=='7':
                a=3
            elif gamma=='6':
                a=2
            elif gamma=='5':
                a=1.5
            else:
                a=1
            val+=a
            if wpn[i] in spaces:
                val+=.25
            if wpro[i]!=None:
                val+=value[wpro[i]]-a
                if Danger:
                    alpha=InDanger(True,wpn[i],multiple=True)
                    if alpha[0]:
                        wdanger.append(value[wpro[i]])
                        if len(alpha[1])>1:
                            wdanger.append(value[wpro[i]])
            else:
                if Danger:
                    alpha=InDanger(True,wpn[i],multiple=True)
                    if alpha[0]:
                        '''if len(alpha[1])==1:
                            if InDanger(True,alpha[1][0]):
                                pass
                            else:        
                                wdanger.append(1)
                        if len(alpha[1])>1:
                            wdanger.append(1)'''
                        wdanger.append(a)
                        if len(alpha[1])>1:
                            wdanger.append(a)
                    
        
        if woth[i]!='None':
            if DetPiece(woth[i])[0]!='King':
                val+=value[DetPiece(woth[i])[0]]
                if woth[i] in spaces:
                    val+=.25
                if Danger:
                    alpha=InDanger(True,woth[i],multiple=True)
                    if alpha[0]:
                        wdanger.append(value[DetPiece(woth[i])[0]])
                        if len(alpha[1])>1:
                            wdanger.append(value[DetPiece(woth[i])[0]])
                        
        if bpn[i]!='None':
            gamma=bpn[i][1]
            if gamma=='2':
                a=3
            elif gamma=='3':
                a=2
            elif gamma=='4':
                a=1.5
            else:
                a=1
            val-=a
            if bpn[i] in spaces:
                val-=.25
            if bpro[i]!=None:
                val-=value[bpro[i]]-a
                if Danger:
                    alpha=InDanger(False,bpn[i],multiple=True)
                    if alpha[0]:
                        bdanger.append(value[bpro[i]])
                        if len(alpha[1])>1:
                            bdanger.append(value[bpro[i]])
            else:
                if Danger:
                    alpha=InDanger(False,bpn[i],multiple=True)
                    if alpha[0]:
                        bdanger.append(a)
                        if len(alpha[1])>1:
                            bdanger.append(a)
        
        if both[i]!='None':
            if DetPiece(both[i])[0]!='King':
                val-=value[DetPiece(both[i])[0]]
                if both[i] in spaces:
                    val-=.25
                if Danger:
                    alpha=InDanger(False,both[i],multiple=True)
                    if alpha[0]:
                        bdanger.append(value[DetPiece(both[i])[0]])
                        if len(alpha[1])>1:
                            bdanger.append(value[DetPiece(both[i])[0]])
    if cCheck:
        if Check(True):
            if color:
                val-=10000
            else:
                val-=2
            if CheckMate(True):
                val-=516
        if Check(False):
            if color:
                val+=2
            else:
                val+=10000
            if CheckMate(False):
                val+=516
    
    if color:
        bdanger.sort()
        bdanger=bdanger[0:len(bdanger)-1]
        val+=max(bdanger)
        val-=max(wdanger)
        return val
    else:
        wdanger.sort()
        wdanger=wdanger[0:len(wdanger)-1]
        val-=max(wdanger)
        val+=max(bdanger)
        return val*-1 
    
passant=False
castlebool=False

AIL1=[]
AIL2=[]
AIL3=[]
AIL4=[]
AIL5=[]
AIL6=[]
AIL7=[]
AIL8=[]
AIL9=[]
AIL10=[]
LL=[AIL1,AIL2,AIL3,AIL4,AIL5,AIL6,AIL7,AIL8,AIL9,AIL10]

def StrAI(color,Ply=1,D=True,FinalPly=1):
    """Given a color, this function determines the move which leaves that player
    with the strongest board as determined by the function, 'Strength.'
    Ply is number of moves and D is whether to include InDanger elements."""
    global w1,w2,w3,b1,b2,b3
    w1t,w2t,w3t,b1t,b2t,b3t=w1,w2,w3,b1,b2,b3
    global Moves
    Moves=[]
    global passant
    global castlebool
    passbool=passant
    castletemp=castlebool
    global LL
    Turn=(FinalPly-Ply+1)
    abc=LL[(Turn+1)/2-1]
    for i in range(16):
        if color:
            L=[]
            L.extend(wpawn)
            L.extend(wother)
        else:
            L=[]
            L.extend(bpawn)
            L.extend(bother)
            
        #L[i] is the location of the piece that is being looked at
        #poss is a list of possible locations that the piece can move
        poss = Possible(L[i])
        temp = L[i]
        if len(poss)>0:
            for j in poss:
                #RestorePoint(10-(FinalPly-Ply))
                if Ply==FinalPly:
                    global J
                    J=j
                if i<8:
                    if color:
                        l=wpawn
                    else:
                        l=bpawn
                elif i>=8:
                    if color:
                        l=wother
                    else:
                        l=bother
                abc=l,temp #l is the list that contains the piece, temp is the temporary location of the piece
                #checks if the move is a passant move
                passant = False
                if DetPiece(j)==None and DetPiece(l[i%8])[0]=='Pawn':
                    try:
                        if color:
                            a=AlphaToNum(j[0])
                            if bpassant[a-1]==k-1 and int(j[1])-1==int(bpawn[a-1][1]):
                                passant = True
                        else:
                            a=AlphaToNum(j[0])
                            if wpassant[a-1]==k-1 and int(j[1])+1==int(wpawn[a-1][1]):
                                passant = True
                    except:
                        pass
                castpiece=None,None
                #print temp,j
                #print castlebool
                if castlebool:
                    if j=='H1':
                        wother[4]='G1'
                        wother[7]='F1'
                        castlemovetemp='F1'
                        castpiece='w',7
                    elif j=='A1':
                        wother[4]='C1'
                        wother[0]='D1'
                        castlemovetemp='D1'
                        castpiece='w',0
                    elif j=='H8':
                        bother[4]='G8'
                        bother[7]='F8'
                        castlemovetemp='F8'
                        castpiece='b',7
                    elif j=='A8':
                        bother[4]='C8'
                        bother[0]='D8'
                        castlemovetemp='D8'
                        castpiece='b',0
                else:
                    l[i%8]=j
                ltake=None
                takeval=0
                
                #begins the code for taking pieces
                if color:
                    for k in range(8):
                        if j==bpawn[k]:
                            bpawn[k]='None'
                            ltake=bpawn
                            c=k
                        elif j == bother[k]:
                            bother[k]='None'
                            ltake=bother
                            c=k
                    if passant==True:
                        a=AlphaToNum(j[0])-1
                        bpawn[a]='None'
                        ltake=bpawn
                        c=a
                else:
                    for k in range(8):
                        if j==wpawn[k]:
                            wpawn[k]='None'
                            ltake=wpawn
                            c=k
                        elif j == wother[k]:
                            wother[k]='None'
                            ltake=wother
                            c=k
                    if passant==True:
                        a=AlphaToNum(j[0])-1
                        wpawn[a]='None'
                        ltake=wpawn
                        c=a
                if Turn==1:
                    cCheck=True
                else:
                    cCheck=False
                #Turn=(FinalPly-Ply+1)
                if Turn<FinalPly:
                    if Turn%2==1 and Turn!=(FinalPly-1):
                        #if it's the opponent's turn, but it's not
                        #the final evaluation
                        """print (Turn+1)/2
                        print bpawn
                        print bother"""
                        RestorePoint((Turn+1)/2)
                        moveval=0
                        JJ=J
                        tempmove=list(Moves)
                        OppMove=StrAI((not color),Ply=1,D=D,FinalPly=1)
                        Moves=list(tempmove)
                        J=JJ
                        Move(OppMove[0],OppMove[1])
                        if Check(color):
                            moveval-=10000
                        #print FinalPly-Ply+1,FinalPly
                        JJ=J
                        tempmove=list(Moves)
                        moveval+=StrAI(color,Ply=Ply-2,D=D,FinalPly=FinalPly)[2]
                        Moves=list(tempmove)
                        J=JJ
                        if Check(color):
                            moveval-=10000
                        #print 'Restoreval:',(Turn+1)/2
                        #Restore((Turn+1)/2)
                        '''print bpawn
                        print bother'''
                        
                    elif Turn==(FinalPly-1):
                        #if this is the final evaluation
                        JJ=J
                        tempmove=list(Moves)
                        OppMove=StrAI((not color),Ply=1,D=D,FinalPly=1)[2]*(-1)
                        Moves=list(tempmove)
                        J=JJ
                        moveval=OppMove
                        if Check(color):
                            moveval-=10000
                        
                elif Turn==FinalPly:
                    moveval=Strength(color,wpawn,wother,bpawn,bother,wpromote,bpromote,Danger=D,cCheck=cCheck)
                Moves.append([temp,J,moveval])# changed this to J instead of j
                l[i%8]=temp
                #print castlebool,'\n'
                if castlebool:
                    if castpiece[0]=='w':
                        castlist=wother
                    elif castpiece[0]=='b':
                        castlist=bother
                    if castpiece[0]!=None:
                        castlist[castpiece[1]]=castlemovetemp
                if ltake!=None:
                    ltake[c]=j
                #Restore(10-(FinalPly-Ply))
    castlebool=castletemp
    passant=passbool
    w1,w2,w3,b1,b2,b3=w1t,w2t,w3t,b1t,b2t,b3t
    Moves.sort(key=GetMax,reverse=True)
    val=Moves[0][2]
    li=[]
    for i in Moves:
        if i[2]==val:
            li.append(i)
    li.sort(key=GetRand)
    #Restore(10-(FinalPly-Ply))
    return li[0][0],li[0][1],val,Moves
            
def GetMax(item):
    return item[2]

def GetRand(item):
    return randint(0,100)

def GetTime(t):
    t=str(t)
    second=float(t[17:24])
    minute=float(t[14:16])
    hour=float(t[11:13])
    return second+minute*60+hour*60**2

def RestorePoint(x):
    """Creates a point where the game can be restored to if needed.
    x should be an int 1-10"""
    global restA,restB,restC,restD,restE,restF,restG,restH,restI,restJ
    L=[restA,restB,restC,restD,restE,restF,restG,restH,restI,restJ]
    l=L[x-1]
    while len(l)<14:
        l.append(0)
    global wpawn
    global bpawn
    global bother
    global wother
    global w1,w2,w3,b1,b2,b3
    global wpassant
    global bpassant
    l[0]=list(wpawn)
    l[1]=list(wother)
    l[2]=list(bpawn)
    l[3]=list(bother)
    l[4]=list(wpromote)
    l[5]=list(bpromote)
    l[6],l[7],l[8],l[9],l[10],l[11]=w1,w2,w3,b1,b2,b3
    l[12]=list(wpassant)
    l[13]=list(bpassant)

def Restore(x):
    global restA,restB,restC,restD,restE,restF,restG,restH,restI,restJ
    L=[restA,restB,restC,restD,restE,restF,restG,restH,restI,restJ]
    l=L[x-1]
    global wpawn
    global bpawn
    global bother
    global wother
    global w1,w2,w3,b1,b2,b3
    global wpassant
    global bpassant
    wpawn = list(l[0])
    wother = list(l[1])
    bpawn = list(l[2])
    bother = list(l[3])
    wpromote = list(l[4])
    bpromote = list(l[5])
    w1,w2,w3,b1,b2,b3=l[6],l[7],l[8],l[9],l[10],l[11]
    wpassant=list(l[12])
    bpassant=list(l[13])

def Move(start,end):
    """Executes a move with all normal results"""
    LL=[wpawn,wother,bpawn,bother]
    for i in LL:
        if start in i:
            l=i
    piece=DetPiece(start)
    #checks if the move is a passant move
    passant = False
    if DetPiece(end)==None and piece[0]=='Pawn':
        try:
            if color:
                a=AlphaToNum(end[0])
                if bpassant[a-1]==k-1 and int(end[1])-1==int(bpawn[a-1][1]):
                    passant = True
            else:
                a=AlphaToNum(end[0])
                if wpassant[a-1]==k-1 and int(end[1])+1==int(wpawn[a-1][1]):
                    passant = True
        except:
            pass
        
    if castlebool:
        if end=='H1':
            wother[4]='G1'
            wother[7]='F1'
        elif end=='A1':
            wother[4]='C1'
            wother[0]='D1'
        elif end=='H8':
            bother[4]='G8'
            bother[7]='F8'
        elif end=='A8':
            bother[4]='C8'
            bother[0]='D8'
    else:
        l[l.index(start)]=end
    color=piece[1]
    if color:
        for k in range(8):
            if end==bpawn[k]:
                bpawn[k]='None'
            elif end == bother[k]:
                bother[k]='None'
        if passant==True:
            a=AlphaToNum(end[0])-1
            bpawn[a]='None'
    else:
        for k in range(8):
            if end==wpawn[k]:
                wpawn[k]='None'
            elif end == wother[k]:
                wother[k]='None'
        if passant==True:
            a=AlphaToNum(end[0])-1
            wpawn[a]='None'

####
# start of the code that runs the game
####

#lists of starting locations of pieces
wpawn=['A2','B2','C2','D2','E2','F2','G2','H2']
wother=['A1','B1','C1','D1','E1','F1','G1','H1']
bpawn=['A7','B7','C7','D7','E7','F7','G7','H7']
bother=['A8','B8','C8','D8','E8','F8','G8','H8']

#sample starting locations for debugging purposes.

"""wpawn=['None','None','C2','D2','E2','F2','None','None']
wother=['None','B1','None','None','E1','None','G1','None']
bpawn=['None','None','C7','D7','E7','F7','None','None']
bother=['None','B8','None','None','E8','None','G8','None']"""


#shows if a certain pawn has been promoted
#the piece name will appear here if so in respective numerical order
wpromote=[None,None,None,None,None,None,None,None]
bpromote=[None,None,None,None,None,None,None,None]

#this tells if a pawn can be taken via an 'en passant' move
wpassant=[None,None,None,None,None,None,None,None]
bpassant=[None,None,None,None,None,None,None,None]

###### Castling;1 is left rook, 2 is king, 3 is right rook
w1=False
w2=False
w3=False
b1=False
b2=False
b3=False
###### boolean denotes whether piece has been moved

###### lists for the Restore functions
restA=[]
restB=[]
restC=[]
restD=[]
restE=[]
restF=[]
restG=[]
restH=[]
restI=[]
restJ=[]
######


k=0
mate=False
mateturn=10**5
draw50=0
stalemate=False
stalemateturn=10**5
AIDifficulty1=1
AIDifficulty2=1

playernum=0
while playernum!=1 and playernum!=2:
    playernum = input('Enter number of players: ')
    print ''
    if playernum!=1 and playernum!=2:
        print 'Please enter a proper number (1 or 2).'
        
while k<mateturn and draw50<51 and k<stalemateturn:
    #k is the turn variable. If k is even at this point, it's white's
    #turn. If k is odd at this point, it's black's turn.
    
    castlebool = False
    passant = False
    bprobool = False
    wprobool = False
    
    if (not mate):
        if k%2==0:
            print "White's Turn\n"
            
            #########
            '''
            if playernum==1:
                a=datetime.now()
                move=StrAI(True,Ply=AIDifficulty1,D=True,FinalPly=AIDifficulty1)
                b=datetime.now()
                time=GetTime(b)-GetTime(a)
                if time<3:
                    AIDifficulty1+=1
                    print AIDifficulty1
                print round(time,3), 's\n'
                start=move[0]
                end=move[1]
                print start
                print end,'\n'
                '''
             #########   
                
        else: 
            print "Black's Turn\n"
            if playernum==1:
                a=datetime.now()
                RestorePoint(10)
                move=StrAI(False,Ply=AIDifficulty2,D=True,FinalPly=AIDifficulty2)
                #global Moves
                #print Moves
                Restore(10)
                b=datetime.now()
                time=GetTime(b)-GetTime(a)
                print round(time,3), 's\n'
                start=move[0]
                end=move[1]
                #print move[3]
                print start
                print end,'\n'
                
            
    k=k+1
    draw50+=1
        
    if (playernum==2 or (playernum==1 and k%2==1)) or mate:
    #if mate:
        MakeWindow(8.5,bgcolor=[0,0,.2],labels=False,Click=True)
        DrawRect(0,0,16,16,FillColor=DARKGRAY)
        for j in range(4):
            for i in range(4):
                DrawRect(-7+4*i,7-4*j,2,2,FillColor=LIGHTGRAY)
                DrawRect(-5+4*i,5-4*j,2,2,FillColor=LIGHTGRAY)
                
        for i in range(1,9):
            DrawText(-8.35,-9+2*i,str(i),FontColor=WHITE)
            s='ABCDEFGH'
            a=s[i-1]
            DrawText(-9+2*i,-8.35,str(a),FontColor=WHITE)
            
        #start drawing the pieces
    
        #white pieces
        wn=0
        for i in wpawn:
            if wpromote[wn]==None:
                val = i
                DrawPawn(val,True)
            elif wpromote[wn]=='Queen':
                val = i
                DrawQueen(val,True)
            elif wpromote[wn]=='Rook':
                val = i
                DrawRook(val,True)
            elif wpromote[wn]=='Bishop':
                val = i
                DrawBishop(val,True)
            elif wpromote[wn]=='Knight':
                val = i
                DrawKnight(val,True)
            wn+=1
        
        DrawRook(wother[0],True)
        DrawKnight(wother[1],True)
        DrawBishop(wother[2],True)
        DrawQueen(wother[3],True)
        DrawKing(wother[4],True)
        DrawBishop(wother[5],True)
        DrawKnight(wother[6],True)
        DrawRook(wother[7],True)
        
        #black pieces
        bn=0
        for i in bpawn:
            if bpromote[bn]==None:
                val = i
                DrawPawn(val,False)
            elif bpromote[bn]=='Queen':
                val = i
                DrawQueen(val,False)
            elif bpromote[bn]=='Rook':
                val = i
                DrawRook(val,False)
            elif bpromote[bn]=='Bishop':
                val = i
                DrawBishop(val,False)
            elif bpromote[bn]=='Knight':
                val = i
                DrawKnight(val,False)
            bn+=1
        
        DrawRook(bother[0],False)
        DrawKnight(bother[1],False)
        DrawBishop(bother[2],False)
        DrawQueen(bother[3],False)
        DrawKing(bother[4],False)
        DrawBishop(bother[5],False)
        DrawKnight(bother[6],False)
        DrawRook(bother[7],False)
        
        #for debugging purposes
        #prints out a list of where each piece can move
        '''
        print 'White Moves'
        for i in wpawn:
            if i=='None':
                pass
            else:
                print i, Possible(i)
        for i in wother:
            if i=='None':
                pass
            else:
                print i, Possible(i)
        print ''
        print 'Black Moves'
        for i in bpawn:
            if i=='None':
                pass
            else:
                print i, Possible(i)
        for i in bother:
            if i=='None':
                pass
            else:
                print i, Possible(i)
        print ''
        '''

        
        ShowWindow()
    
    #if there is no checkmate, this portion will allow
    #for the input of a move and subsequent changes
    if (not mate) and (not stalemate) and draw50<50:
        #control panel of the game
        if playernum==2 or (playernum==1 and k%2==1):
        #if False:
            with open('chessmove.txt', 'r') as F:
                data = F.readlines()
                L=[]
                for j in data:
                    if j!='':
                        s1=j.rstrip('\n')
                        s2=s1.strip('\r')
                        L.append(s2)
                if len(L)>0:
                    code = L[0]
                    if code.upper()=='QUIT':
                        quit()
            
            #reads input from the text doc (click edition)
            with open('mousetext.txt', 'r') as F:
                data = F.readlines()
                L=[]
                start=None
                end=None
                for j in data:
                    if j!='':
                        s1=j.rstrip('\n')
                        s2=s1.strip('\r')
                        L.append(s2)
                try:
                    a=L[0].split(' ')
                    b=L[1].split(' ')
                    start=reversemap(a)
                    end=reversemap(b)
                except:
                    print 'Not a valid move.\n'
                    print 1471
                    
            #clears the text doc
            with open('mousetext.txt', 'w') as F:
                F.write('')
        
        #if there is a proper number of coordinates selected, this portion is run
        if end != None:
            #gives the ability to quit the game without the text document 
            if start=='A0' and end=='H1':
                quit()
            
            #determines whether a piece of the correct color was selected
            turnbool=True
            if k%2==1:
                for i in range(8):
                    if start==bpawn[i] or start==bother[i]:
                        turnbool=False
                        count=8
            else:
                for i in range(8):
                    if start==wpawn[i] or start==wother[i]:
                        turnbool=False
                        count=8
            
            #Applies the move contstraints and sets the variable
            #'legal' to the boolean legality of the move
            piece=DetPiece(start) #contains a tuple of color bool and piece name string
            legal=True
            if piece==None:
                legal=False
            elif piece[0]=='Pawn':
                legal=PawnMove(piece[1],start,end)
            elif piece[0]=='Rook':
                legal=RookMove(piece[1],start,end)
            elif piece[0]=='Bishop':
                legal=BishopMove(piece[1],start,end)
            elif piece[0]=='Queen':
                legal=QueenMove(piece[1],start,end)
            elif piece[0]=='Knight':
                legal=KnightMove(piece[1],start,end)
            elif piece[0]=='King':
                legal=KingMove(piece[1],start,end)
                try:
                    if piece[0]=='King' and DetPiece(end)[0]=='Rook' and piece[1]==DetPiece(end)[1]:
                        legal=Castle(piece[1],start,end)
                        if legal:
                            castlebool=True
                            passant=False
                except:
                    pass
        
            #if the move is legal, this changes the location of the piece selected
            #and allows for pieces to be taken
            if legal:
                #creating temporary lists of locations in case
                #the move ends up in check
                wpawntemp=list(wpawn)
                wothertemp=list(wother)
                bpawntemp=list(bpawn)
                bothertemp=list(bother)
                wpromotetemp=list(wpromote)
                bpromotetemp=list(bpromote)
                w1t,w2t,w3t,b1t,b2t,b3t=w1,w2,w3,b1,b2,b3
    
                #changes location of the piece selected
                if turnbool:
                    bprobool=False
                    wprobool=False
                    count = 0
                    for i in range(8):
                        if castlebool:
                            if end=='H1':
                                wother[4]='G1'
                                wother[7]='F1'
                            elif end=='A1':
                                wother[4]='C1'
                                wother[0]='D1'
                            elif end=='H8':
                                bother[4]='G8'
                                bother[7]='F8'
                            elif end=='A8':
                                bother[4]='C8'
                                bother[0]='D8'
                        elif start == wpawn[i]:
                            wpawn[i]=end
                            #checks if a pawn needs promotion (below)
                            draw50=0
                            if end[1]=='8' and wpromote[i]==None:
                                wloc=i
                                wprobool=True
                        elif start == wother[i]:
                            wother[i]=end
                        elif start == bpawn[i]:
                            bpawn[i]=end
                            #checks if a pawn needs promotion (below)
                            draw50=0
                            if end[1]=='1' and bpromote[i]==None:
                                bloc=i
                                bprobool=True
                        elif start == bother[i]:
                            bother[i]=end
                        else:
                            count = count + 1
                if count == 8:
                    print 'Not a valid move.\n'
                    print 1576
                    k=k-1
                
                #code for taking pieces
                else:
                    if k%2==1:
                        for i in range(8):
                            if end==bpawn[i]:
                                bpawn[i]='None'
                                draw50=0
                            elif end == bother[i]:
                                bother[i]='None'
                                draw50=0
                        if passant==True:
                            temp=AlphaToNum(end[0])-1
                            bpawn[temp]='None'
                            draw50=0
                    if k%2==0:
                        for i in range(8):
                            if end==wpawn[i]:
                                wpawn[i]='None'
                                draw50=0
                            elif end == wother[i]:
                                wother[i]='None'
                                draw50=0
                        if passant==True:
                            temp=AlphaToNum(end[0])-1
                            wpawn[temp]='None'
                            draw50=0

                ### changes to evaluate if castling is allowed
                if start=='A1':
                    w1=True
                elif start=='E1':
                    w2=True
                elif start=='H1':
                    w3=True
                elif start=='A8':
                    b1=True
                elif start=='E8':
                    b2=True
                elif start=='H8':
                    b3=True
                ###
                
                #code that tests if the resulting move makes that person in check
                #if check occurs, the piece locations are reset using the temp lists
                if k%2==1:
                    c=True
                else:
                    c=False
                if Check(c):
                    print 'Not a valid move.\n'
                    print 1629
                    k=k-1
                    wpawn = wpawntemp
                    wother = wothertemp
                    bpawn = bpawntemp
                    bother = bothertemp
                    wpromote = wpromotetemp
                    bpromote = bpromotetemp
                    w1,w2,w3,b1,b2,b3=w1t,w2t,w3t,b1t,b2t,b3t
            
            else:
                print 'Not a valid move.\n'
                k=k-1
                print 1642
                #quit()
        
        else:
            k=k-1
        
        #this is for entering the piece that a pawn is promoted to
        if bprobool:
            bx=''
            if playernum==1:
                bpromote[bloc]='Queen'
                bprobool=False
            else:
                while bx!='Queen' and bx!='Bishop' and bx!='Rook' and bx!='Knight':
                    bx=raw_input('Enter the piece that you want (Queen, Rook, Bishop, Knight): ')
                    bx=bx[0].upper() + bx[1:].lower()
                    if bx!='Queen' and bx!='Bishop' and bx!='Rook' and bx!='Knight':
                        print '\nPlease enter an appropriate piece.\n'
                bpromote[bloc]=bx
                bprobool=False
            
        if wprobool:
            wx=''
            
            ########
            '''
            if playernum==1:
                bpromote[bloc]='Queen'
                bprobool=False
                '''
                ##########
                
            while wx!='Queen' and wx!='Bishop' and wx!='Rook' and wx!='Knight':
                wx=raw_input('Enter the piece that you want (Queen, Rook, Bishop, Knight): ')
                wx=wx[0].upper() + wx[1:].lower()
                if wx!='Queen' and wx!='Bishop' and wx!='Rook' and wx!='Knight':
                    print '\nPlease enter an appropriate piece.\n'
            wpromote[wloc]=wx
            wprobool=False

        #code for 'check' notification
        if k%2==1:
            c=False
        else:
            c=True
        if Check(c):
            if c:
                s = 'White'
            else:
                s = 'Black'
            if CheckMate(c):
                print 'Checkmate!\n'
                mate=True
                mateturn=k+1
            else:
                print s + ' is in check.\n'
        else: 
            if CheckMate(c):
                stalemate=True
                print 'Stalemate.'
                stalemateturn=k+1
                



