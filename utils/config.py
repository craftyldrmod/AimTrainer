import json
import pygame as pg

from typeObjects.size import Size




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


