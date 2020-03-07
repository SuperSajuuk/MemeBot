# Memes
import random
tweets = [
	"https://twitter.com/TheJepsquad/status/1049833765223182336",
	"https://twitter.com/TheJepsquad/status/1052393566608285696",
	"https://twitter.com/TheJepsquad/status/1052387037561663489",
	"https://twitter.com/TheJepsquad/status/1048362203617742848",
	"https://twitter.com/TheJepsquad/status/1083896926419013632",
	"https://twitter.com/TheJepsquad/status/1088578519154733056",
	"https://twitter.com/TheJepsquad/status/1119443773946200064",
	"https://twitter.com/TheJepsquad/status/1130316651969294337",
	"https://twitter.com/TheJepsquad/status/1130307154647371777",
	"https://twitter.com/TheJepsquad/status/1126458582541664256",
	"https://twitter.com/TheJepsquad/status/1123303322658779136",
	"https://twitter.com/TheJepsquad/status/1123054964119674880",
	"https://twitter.com/TheJepsquad/status/1121070244360007680",
	"https://twitter.com/TheJepsquad/status/1120872966336733185",
	"https://twitter.com/TheJepsquad/status/1118895136811962369",
	"https://twitter.com/TheJepsquad/status/1113557049785368577",
	"https://twitter.com/TheJepsquad/status/1109499586220036099",
	"https://twitter.com/TheJepsquad/status/1111791030288957441",
	"https://twitter.com/TheJepsquad/status/1093330044511023106",
	"https://twitter.com/TheJepsquad/status/1090729412390203393",
	"https://twitter.com/TheJepsquad/status/1088981503529414656",
	"https://twitter.com/TheJepsquad/status/1131668615403646976",
	"https://twitter.com/TheJepsquad/status/1133553878224560128",
	"https://twitter.com/TheJepsquad/status/1143295120340606976",
	"https://twitter.com/FireLordBrooke/status/1126352366024790016",
	"https://twitter.com/platicorn_/status/1028167009647910912",
	"https://twitter.com/platicorn_/status/999497073249669122"
]

clips = [
	"https://clips.twitch.tv/SmilingAssiduousBearSoonerLater",
	"https://clips.twitch.tv/EnthusiasticManlyHamWow",
	"https://clips.twitch.tv/GeniusEnthusiasticManateeKappaPride",
	"https://clips.twitch.tv/StrangeImpossibleKathyResidentSleeper",
	"https://clips.twitch.tv/BraveBlatantTapirPogChamp",
	"https://clips.twitch.tv/CovertAntsyTurtleBudBlast",
	"https://clips.twitch.tv/CallousAbstruseSparrowFreakinStinkin",
	"https://clips.twitch.tv/ObliqueColdbloodedCardThisIsSparta",
	"https://clips.twitch.tv/BreakableCrepuscularSwordDansGame",
	"https://clips.twitch.tv/PrettiestPowerfulCakeKappa",
	"https://clips.twitch.tv/RoundLazyManateeTriHard",
	"https://clips.twitch.tv/EnergeticSilkyHawkDeIlluminati",
	"https://clips.twitch.tv/ThirstyThankfulSharkOSsloth",
	"https://clips.twitch.tv/BlazingDepressedPigeonYee",
	"https://clips.twitch.tv/JazzyCrispySnoodThunBeast",
	"https://clips.twitch.tv/CloudyCourageousThymeDBstyle",
	"https://clips.twitch.tv/CaringSincereClipzOSsloth",
	"https://clips.twitch.tv/RepleteDignifiedTireDancingBanana",
	"https://clips.twitch.tv/WiseVenomousPuddingPermaSmug",
	"https://clips.twitch.tv/ThankfulTriumphantBaconWOOP",
	"https://clips.twitch.tv/CovertFreezingNostrilWow",
	"https://clips.twitch.tv/AgreeableUnusualOwlImGlitch",
	"https://clips.twitch.tv/SlickEndearingKathyPJSalt",
	"https://clips.twitch.tv/ApatheticAverageKoalaBleedPurple",
	"https://clips.twitch.tv/PleasantColorfulSlothYee",
	"https://clips.twitch.tv/BreakableCrepuscularSwordDansGame",
	"https://clips.twitch.tv/ClumsySparklyKiwiTBTacoLeft",
	"https://clips.twitch.tv/HealthySweetSoymilkDatSheffy",
	"https://clips.twitch.tv/ToughIncredulousOpossumRalpherZ",
	"https://clips.twitch.tv/AdventurousSweetWrenchWoofer"
]

images = [
	"https://cdn.discordapp.com/attachments/167887890003656704/531292294264127509/Josh_Face.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531292510111399961/Screenshot_109.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531292672921567242/AlexPenis.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531292689359044608/Bad_night.png"
	"https://cdn.discordapp.com/attachments/167887890003656704/531292751971483649/Do_the_doctor.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531292822058434571/Sharp_7777.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531292854530605088/Screenshot_20180726-0025062.png",
	"https://cdn.discordapp.com/attachments/123237433197330432/531293354189914127/DrHx_NeU0AA3Axf.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531294414480605255/DntPs8-U8AAR3dR.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531294556507996160/DnvoDbWVsAABITl.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531294596349820939/DnrdhyWUcAEHx52.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/529501904573693970/unknown.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531295105399914526/unknown.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531295268591632384/2018-08-05_2.png",
	"https://cdn.discordapp.com/attachments/167887890003656704/531652730884849692/image0.jpg",
	"https://cdn.discordapp.com/attachments/531618142942789653/649330349708673036/JoshFU.png",
	"https://cdn.discordapp.com/attachments/381200080796909568/637129745351311361/youngjosh.jpg",
	"https://cdn.discordapp.com/attachments/356691457068761089/637363882112843806/unknown.png",
	"https://cdn.discordapp.com/attachments/123237433197330432/583110865138483241/emoji.png",
	"https://cdn.discordapp.com/attachments/123237433197330432/673631778631843849/image0.gif"
]

other = [
	"https://youtu.be/LRu3NcDoW3Y",
	"Creepy faces: https://discordapp.com/channels/123237433197330432/131498268990373889/526177459087867907",
	"https://cdn.discordapp.com/attachments/356691457068761089/629868932966121482/GlimwoodRace.mp4",
	"https://cdn.discordapp.com/attachments/356691457068761089/628663100215656448/JepsonCatScream.mp4",
	"https://cdn.discordapp.com/attachments/356691457068761089/586766090789715969/OffTheMountain.mp4",
	"https://t.co/YmLqhMcrLD"
]

def getRandomMeme():
	memes = tweets + clips + images + other
	return random.choice(memes)
	
def getRandomTweet():
	return random.choice(tweets)
	
def getRandomImage():
	return random.choice(images)
	
def getRandomClip():
	return random.choice(clips)
	
def getRandomSomething():
	return random.choice(other)