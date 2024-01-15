#!/usr/bin/python3

import json
import csv
import turtle


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            list_dicts = [o.to_dictionary() for o in list_objs] if list_objs else []
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string and json_string != "[]" else []

    @classmethod
    def create(cls, **dictionary):
        if dictionary:
            new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs:
                fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        def draw_shape(turt, color, obj):
            turt.showturtle()
            turt.up()
            turt.goto(obj.x, obj.y)
            turt.down()
            for _ in range(2):
                turt.forward(obj.width)
                turt.left(90)
                turt.forward(obj.height)
                turt.left(90)
            turt.hideturtle()

        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            draw_shape(turt, "#ffffff", rect)

        turt.color("#b5e3d8")
        for sq in list_squares:
            draw_shape(turt, "#b5e3d8", sq)

        turtle.exitonclick()

