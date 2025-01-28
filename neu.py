import tkinter
import time

def rgb_to_tkinter_color(r, g, b):
    return f'#{r*257:04x}{g*257:04x}{b*257:04x}'

class Point:
    points: list = []

    def __init__(self, pos_x: float, pos_y: float):
        self.__x = pos_x
        self.__y = pos_y
        Point.points.append(self)

    @property
    def x(self) -> float:
        return self.__x
    @property
    def y(self) -> float:
        return self.__y
    

class Window:
    rects: list = []

    def __init__(self, width, height, title):
        self.__handle = tkinter.Tk()
        self.__width = width
        self.__height = height
        self.__handle.title(title)
        self.__handle.geometry(f"{width}x{height}+20-100")
        self.__canvas = tkinter.Canvas(self.__handle, height=height, width=width)
        self.canvas.pack()

    @property
    def canvas(self):
        return self.__canvas
    @property
    def handle(self):
        return self.__handle
    
    def create_rect(self, p1: Point, p2: Point):
        self.rects.append( self.__canvas.create_rectangle(p1.x, p1.y, p2.x, p2.y, outline="orange", fill=rgb_to_tkinter_color(255,255,0) ) )
    
    def recolor(self, rect_id, color):
        self.canvas.itemconfig(rect_id, fill=color)
    # def rmove(self, x, y):
    #     for item in self.rects:
    #         self.canvas.move(item, x, y)
    
    def update(self):
        self.handle.update_idletasks()
        self.handle.update()
        self.canvas.pack()


def generate_fibonacci(limit: int = 500) -> list:
    cur = 0
    next = 1
    seq: list = []
    while cur < limit:
        seq.append(cur)
        cur = next
        next += seq[-1]
    return seq


def fib_spiral(win: Window, sequence: list[int], step: int, start_point: Point):
    dir = step % 4
    if step < len(sequence):
        if dir == 0:
            end_point = Point( start_point.x + sequence[step], start_point.y + sequence[step] )
        elif dir == 1:
            end_point = Point( start_point.x + sequence[step], start_point.y - sequence[step] )
        elif dir == 2:
            end_point = Point( start_point.x - sequence[step], start_point.y - sequence[step] )
        elif dir == 3:
            end_point = Point( start_point.x - sequence[step], start_point.y + sequence[step] )

        win.create_rect( start_point, end_point )
        return end_point


def main(width: int = 800, height: int = 600, title: str = "n/a") -> int:
    window = Window(width, height, title)
    step = 0
    start_point = Point(int(width / 2), int(height / 2))
    sequence = generate_fibonacci(2000)
    timer = 0.085
    while True:
        if step < len(sequence):
            start_point = fib_spiral(window, sequence, step, start_point)
        else:
            window.recolor(step - len(sequence), rgb_to_tkinter_color(192, 96, 0))
            if step > 2 * len(sequence):
                break

        step += 1
        #window.rmove(randint(-3,3),randint(-3,3))
        window.update()
        time.sleep(timer)
        timer += 0.005


if __name__ == "__main__":
    width = 1024
    height = 768
    main(width, height, "test")