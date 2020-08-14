import random
# type: ignore
import nekos


def get_neko_sfw() -> str:
    possible = ['waifu', 'fox_girl', 'neko', 'cuddle']
    return str(nekos.img(random.choice(possible)))


def get_neko_nsfw() -> str:
    possible = [
        'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
        'solog', 'feetg', 'cum', 'les', 'lewdk', 'lewd', 'cum_jpg', 'bj', 
        'nsfw_neko_gif', 'solo', 'nsfw_avatar', 'anal', 'hentai', 'erofeet',
        'blowjob', 'pussy', 'tits', 'pussy_jpg',
        'pwankg', 'classic', 'kuni', 'femdom',
        'spank', 'erok', 'boobs', 'random_hentai_gif',
        'smallboobs']
    nsfw_neko_img = str(nekos.img(random.choice(possible)))
    while str(404) in nsfw_neko_img:
        nsfw_neko_img = str(nekos.img(random.choice(possible)))
    return nsfw_neko_img


class NekoActions:
    def neko_slap(self) -> str:
        self.slap_image_url = str(nekos.img('slap'))
        return self.slap_image_url

    def neko_kiss(self) -> str:
        self.kiss_image_url = str(nekos.img('kiss'))
        return self.kiss_image_url

    def neko_pat(self) -> str:
        self.pat_image_url = str(nekos.img('pat'))
        return self.pat_image_url

    def neko_cuddle(self) -> str:
        self.cuddle_image_url = str(nekos.img('cuddle'))
        return self.cuddle_image_url

    def neko_hug(self) -> str:
        self.hug_image_url = str(nekos.img('hug'))
        return self.hug_image_url

    def neko_tickle(self) -> str:
        self.tickle_image_url = str(nekos.img('tickle'))
        return self.tickle_image_url


def owo_text(desired_text: str) -> str:
    return str(nekos.owoify(desired_text))
