import time, os, sys

class StopWatch():
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self):        
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = ""               
        self.Start()    

    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)                
        self.timestr = '%02d:%02d' % (minutes, seconds)

    def getTime(self):
        return self.timestr
        
    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:           
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
