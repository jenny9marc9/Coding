checking <- function(Field){
  c1=c(2,2,2)
  c2=c(3,3,3)
  x <- 0
  if(identical(c(Field[3,1],Field[2,2],Field[1,3]),c1)==TRUE){
    x=1
  }
  if(identical(c(Field[3,1],Field[2,2],Field[1,3]),c2)==TRUE){
    x=2
  }
  if(identical(diag(Field),c1)==TRUE){
    x=1
  }
  if(identical(diag(Field),c2)==TRUE){
    x=2
  }
  for(n in 1:3){
    if(identical(Field[n,],c1)==TRUE|| identical(Field[,n],c1)==TRUE){
      x=1
    }
  }
  for(n in 1:3){
    if(identical(Field[n,],c2)==TRUE || identical(Field[,n],c2)==TRUE){
      x=2
    }
  }
  if(min(Field)>1 & x==0){
    x=3
  }
  return(x)
}
#Lets start the game
TicTacToe1 <- function(){
  
  color <- c('white','forestgreen','red')
  Field <- matrix(1,3,3)
  par(xaxt='n',yaxt='n')
  image(x=1:3,y=1:3,Field,col=color,
        zlim=c(1,3),xlab='',ylab='')
  abline(h=c(1.5,2.5),v=c(1.5,2.5),col='gray')
  
  x <- 0

  while(x==0){
    tmp <- locator(1)
    if(Field[round(tmp$x),round(tmp$y)]==1){
      Field[round(tmp$x),round(tmp$y)] <- 2
      image(x=1:3,y=1:3,Field,col=color,
            zlim=c(1,3),xlab='',ylab='')
      abline(h=c(1.5,2.5),v=c(1.5,2.5),col='gray')
    }
    x <- checking(Field)
    if(x==1){
      y='you win'
    }

    if(x==0){
      available <- which(Field==1)
      C <- sample(available,size=1)
      Field[C] <- 3
      image(x=1:3,y=1:3,Field,col=color,
            zlim=c(1,3),xlab='',ylab='')
      abline(h=c(1.5,2.5),v=c(1.5,2.5),col='gray')
      x <- checking(Field)
      if(x==2){
        y='you lose'
      }
    }
  }
  x=checking(Field)
  if(x==3){
    y='it is a draw'
  }
  return(y)
}

TicTacToeSeries <- function(){
  ready <- readline('Are you ready? (yes/no)   ')
  if(as.character(ready)=='yes'){
    w=c(0,0,0)
    while(as.character(ready)=='yes'){
      y=TicTacToe1()
      print(y)
      if(y=='P'){
        w[1]=w[1]+1
      }
      if(y=='C'){
        w[2]=w[2]+1
      }
      if(y=='N'){
        w[3]=w[3]+1
      }
      ready <- readline('do you wanna play again? (yes/no)   ')
    }
  return(data.frame(result=c('player wins','computer wins','draws'),number=w))
  }
}

TicTacToeFuture <- function(){
  
  color <- c('white','forestgreen','red')
  Field <- matrix(1,3,3)
  par(xaxt='n',yaxt='n')
  image(x=1:3,y=1:3,Field,col=color,
        zlim=c(1,3),xlab='',ylab='')
  abline(h=c(1.5,2.5),v=c(1.5,2.5),col='gray')
  
  x=0
  
  while(x==0){
    tmp <- locator(1)
    if(Field[round(tmp$x),round(tmp$y)]==1){
      Field[round(tmp$x),round(tmp$y)] <- 2
      image(x=1:3,y=1:3,Field,col=color,
            zlim=c(1,3),xlab='',ylab='')
      abline(h=c(1.5,2.5),v=c(1.5,2.5),col='gray')
    }
    x=checking(Field)
    if(x==1){
      y='P1'
    }
    
    if(x==0){
      tmp <- locator(1)
      if(Field[round(tmp$x),round(tmp$y)]==1){
        Field[round(tmp$x),round(tmp$y)] <- 3
        image(x=1:3,y=1:3,Field,col=color,
              zlim=c(1,3),xlab='',ylab='')
        abline(h=c(1.5,2.5),v=c(1.5,2.5),col='gray')
      }
      x=checking(Field)
      if(x==2){
        y='P2'
      }
    }
  }
  x=checking(Field)
  if(x==3){
    y='N'
  }
  
  return(y)
  
}

TicTacToe1()
TicTacToeSeries()
TicTacToeFuture()   

