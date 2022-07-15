import json
import pygame as pg

from typeObjects.size import Size
from typeObjects.color import Color




class Config:
    def getTexture(objectName:str) -> pg.Surface:
        with open('./config.json', 'r') as _config:
            config = json.load(_config)
            
            path = config['textures_path'] + config['texture_map'][objectName]
            img = pg.image.load(path)

            return img

    def getWindowSize() -> Size:
        with open('./config.json', 'r') as _config:
            config = json.load(_config)

            return Size(config['window']['width'], config['window']['height'])

    def getBackgroundColor() -> Color:
        with open('./config.json', 'r') as _config:
            config = json.load(_config)

            return Color(*config['window']['background_color'])

    def getRandSize() -> bool:
        with open('./config.json', 'r') as _config:
            config = json.load(_config)

            return config['random_size']

    def getRandSizeRange() -> dict[str:list, str:list]:
        with open('./config.json', 'r') as _config:
            config = json.load(_config)

            return config['random_size_range']


