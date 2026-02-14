class ProgressBar:
  def __init__(self):
    self.graph = ["0        20        40        60        80       100",
                  "|----+----|----+----|----+----|----+----|----+----|"]
    
    self.track = "="
    
    self.render_gui()

  def render_gui(self):
    for row in self.graph:
      print(row)
        
    print(self.track, end='\r')
 
  def update(self, percentage_value):
    progress = percentage_value // 2
    
    self.render_track(progress)
    
    if percentage_value == 100:
      print("\n\nCompleted! All files renamed.")

  def render_track(self, progress):
    print("{}".format(self.track * (progress + 1)), end='\r')
