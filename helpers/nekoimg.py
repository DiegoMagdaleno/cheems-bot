import random
import nekos
def get_neko_sfw():
        possible = ['waifu', 'fox_girl', 'neko', 'cuddle']
        return nekos.img(random.choice(possible))
    
def get_neko_nsfw():
    possible = [
        'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
        'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
        'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron',
        'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
        'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo',
        'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg',
        'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom',
        'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif',
        'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']
    return nekos.img(random.choice(possible))

def get_neko_slap():
        possible = ['slap']
        return nekos.img(random.choice(possible))

def get_neko_kiss():
        possible = ['kiss']
        return nekos.img(random.choice(possible))

def get_neko_pat():
        possible = ['pat']
        return nekos.img(random.choice(possible))

def get_neko_cuddle():
        possible = ['cuddle']
        return nekos.img(random.choice(possible))

def owo_text(desired_text):
    return nekos.owoify(desired_text)

#def get_neko_sfw():
#        possible = ['wallpaper', 'slap', 'waifu', 'pat', 'kiss', 'fox_girl',
#        'neko', 'cuddle']
#        return nekos.img(random.choice(possible))
# just putting this here so i can refer to it later :)