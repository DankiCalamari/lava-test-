import discord
from discord.ext import commands
from discord.ext.commands import command
import random

client = commands.Bot(command_prefix = 'l~')
client.remove_command('help')

 
@client.group()
async def rps(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Please state what you want to use. E.g. `.rps rock`')
        

@rps.command()
async def rock(ctx):
    choices = ["I use Rock, it's a draw!", "I use Paper, I win!", "I use scissors, you win!"]
    await ctx.send(random.choice(choices))
    
@rps.command()
async def paper(ctx):
    choices = ["I use Rock, you win!", "I use Paper, it's a draw!", "I use scissors, I win!"]
    await ctx.send(random.choice(choices))
    
@rps.command()
async def scissors(ctx):
    choices = ["I use Rock, I win!", "I use Paper, you win!", "I use Scissors, it's a draw!"]
    await ctx.send (random.choice(choices))

@client.group()
async def help(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(
            colour = discord.Colour.green())
        embed=discord.Embed(title="Need help? This is the right place!", description="Lava 2020")
        embed.set_author(name="Lava Help")
        embed.add_field(name="Moderation", value="`l~help moderation`    ", inline=False)
        embed.add_field(name="Fun", value="`l~help fun`", inline=False)
        embed.add_field(name="Utility", value="`l~help utility`", inline=False)
        embed.add_field(name="Other", value="`l~help other`", inline=False)
        embed.set_footer(text="Lava 2020")
        await ctx.send(embed=embed)

@help.command()
async def moderation(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed=discord.Embed(title="Need help? This is the right place!", description="Lava 2020")
    embed.set_author(name="Lava Help")
    embed.add_field(name="Ban", value="`l~ban {user mention}` - *You swing the ban hammer*", inline=False)
    embed.add_field(name="Kick", value="`l~kick {user mention}` - *You boot someone in the a***", inline=False)
    embed.add_field(name="Mute", value="`l~mute {user mention}` Silence someone (Required Muted role to be premade)", inline=False)
    embed.add_field(name="Unmute", value="`l~unmute {user mention}` - Un-silence someone (Requires Muted role to be premade)", inline=True)
    embed.set_footer(text="Lava 2020 - Danki co.")
    await ctx.send(embed=embed)
    
@help.command()
async def fun(ctx):
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed=discord.Embed(title="Need help? This is the right place!", description="Lava 2020")
    embed.set_author(name="Lava Help - Fun")
    embed.add_field(name="Rock Paper Scissors", value="`l~rps {rock, paper or scissors}`", inline=True)
    embed.add_field(name="Coin flip", value="`l~coinflip` Flips a coin to decide your fate.", inline=True)
    embed.add_field(name="Image", value="`l~image {pokemon, cats, redpanda, LRImage}` Images in an embed, fancy.", inline=True)
    embed.add_field(name="Meme", value="`l~meme` Memes or Me-mes?", inline=True)
    embed.add_field(name="Hug", value="`l~hug {member}` Hug someone without risking getting sick! ", inline=True)
    embed.add_field(name="Say", value="`l~say {argument}` Warning: This only allows one argument", inline=True)
    embed.add_field(name="Lemonrant", value="`l~Lemonrant Image Sends Lemon Rant As A Image", inline=True)
    embed.add_field(name="Lemonrant", value="`l~Lemonrant text Sends Lemon Rant As Text", inline=True)
    embed.set_footer(text="Lava 2020")
    await ctx.send(embed=embed)
    
@help.command()
async def utility(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed=discord.Embed(title="Need help? This is the right place!", description="Lava 2020")
    embed.set_author(name="Lava Help")
    embed.add_field(name="Server Name", value="`l~server`", inline=False)
    embed.add_field(name="Server Owner", value="`l~server owner`", inline=False)
    embed.add_field(name="Name", value="`l~name {name}`", inline=False)
    embed.set_footer(text="Lava 2020")
    await ctx.send(embed=embed)
    
@help.command()
async def other(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed=discord.Embed(title="Need help? This is the right place!", description="Lava 2020")
    embed.set_author(name="Lava Help")
    embed.add_field(name="Credits", value="`.credits` - Credits of the bot. Bot owner and who supplied the source code.", inline=False)
    embed.add_field(name="Ping", value="`l~ping` - The Bots Ping.", inline=False)
    embed.add_field(name="Server Owner", value="`l~website` - The Website! (finally got one!)", inline=False)
    embed.set_footer(text="Lava 2020")
    await ctx.send(embed=embed)
    
@client.group()
async def server(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(
            color = discord.Colour.red())
        embed.set_author(name=f'The server name is {ctx.guild.name}')
        await ctx.send(embed=embed)

@server.command()
async def owner(ctx):
    embed = discord.Embed(
        colour = discord.Colour.red()) 
    embed.set_author(name=f'The server owner is: {ctx.guild.owner.name}')
    await ctx.send(embed=embed)

@client.command()
async def name(ctx, member:discord.Member = None):
    choices = ["https://www.icegif.com/wp-content/uploads/love-hug-icegif.gif", "https://acegif.com/wp-content/uploads/anime-hug.gif", "https://media2.giphy.com/media/JUwliZWcyDmTQZ7m9L/200_d.gif"]
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed.set_author(name=f"{member}\nThis is probably a useless command.")
    if not member:
        await ctx.send(f"You forgot to state the name!")
        return
    await ctx.send(embed=embed)
    
    
@client.event
async def on_ready():
    choices = ["Epic, Lava is up.", "Nice job man!"]
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="spooktober from home | l~help"))
                                                           
@client.group()
async def image(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(
            colour = discord.Colour.red())
        embed=discord.Embed(title="404", description="Image not found. Did you forget to enter what you wanted, mis-spell the what you wanted, or what you want is not in our database.")
        embed.set_image(url="https://static-cse.canva.com/blob/133600/10.23129d32.jpg")
        await ctx.send(embed=embed)

@image.command()
async def pokemon(ctx):
    choices = ["https://compote.slate.com/images/18ba92e4-e39b-44a3-af3b-88f735703fa7.png?width=780&height=520&rect=1560x1040&offset=0x0", "https://oyster.ignimgs.com/mediawiki/apis.ign.com/pokemon-switch/e/ea/Grookey.jpg"]
    embed = discord.Embed(
        color = discord.Colour.purple())
    embed.set_author(name='Here is your Pokémon image!')
    embed.set_image(url=random.choice(choices))
    await ctx.send(embed=embed)
    
    
@client.command()
async def lrtext(ctx):

	embed = discord.Embed(title="Lemon Rant!", description="I’ve been thinking. When life gives you lemons? Don’t make lemonade. Make life take the lemons back! Get mad! I don’t want your damn lemons! What am I supposed to do with these? Demand to see life’s manager! Make life rue the day it thought is could give me lemons! Do you know who I am? I’m the man who’s going to burn your house down! With the lemons! I’m going to get my engineers to invent a combustible lemon that burns your house down!",      color=discord.Color.red())
  
 embed.set_footer(text="Please Dont Give Him Lemons")

	await ctx.channel.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member, or I am unable to do my job.")
        return
    await member.kick()
    await ctx.send(f"{member.mention} got kicked. ")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people. If this is a mistake, please DM ^~(◔◡◔) ♥ Danki_RAWR.exe ♥~^#0316")

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member, or I am unable to do my job.")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got banned. BIG OOF")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people. If this is a mistake, please DM ^~(◔◡◔) ♥ Danki_RAWR.exe ♥~^#0316")
        
@client.command()
async def hug(ctx, member:discord.Member = None):
    choices = ["https://www.icegif.com/wp-content/uploads/love-hug-icegif.gif", "https://acegif.com/wp-content/uploads/anime-hug.gif", "https://media2.giphy.com/media/JUwliZWcyDmTQZ7m9L/200_d.gif"]
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed.set_author(name=f"{member} got hugged, awwww!")
    embed.set_image(url=random.choice(choices))
    if not member:
        embed2 = discord.Embed(
            colour = discord.Colour.purple())
        embed.set_author(name=f"Please specify a member, {member}!")
        embed.set_image(url="https://thumbs.gfycat.com/PalatableLimpBanteng-small.gif")
        await ctx.send(f"Hug failed to send. Whyyyyy tho {member.mention}")
        return
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member, or I am unable to do my job.")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people. If this is a mistake, please DM ^~(◔◡◔) ♥ Danki_RAWR.exe ♥~^#0316")

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member, or I am unable to do my job.")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people. If this is a mistake, please DM ^~(◔◡◔) ♥ Danki_RAWR.exe ♥~^#0316")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
   
@client.command()
async def update(ctx):
    await ctx.send("__Hello!__\n\nSorryry for the Lava outage! I posted the token to the public (Stupid, I know), therfore, Lava went offline.\n\n- LavaDev")


    
@client.command()
async def credits(ctx):
    await ctx.send(f'__**Bot Developer**__\n\n^~(◔◡◔) ♥ Danki_RAWR.exe ♥~^#0316')

@client.command()
async def website(ctx):
    await ctx.send(f'__Website__\n\nhttps://lavabotdeveloper.github.io/LavaDevWebsite/')

@client.command()
async def support(ctx):
    await ctx.send(f'__Support Discord__\n\nhttps://discord.gg/qP7cSde')


@image.command(pass_context=True)
async def cats(ctx):
    choices = ["https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg", "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg", "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/reference_guide/outdoor_cat_risks_ref_guide/1800x1200_outdoor_cat_risks_ref_guide.jpg", "https://www.cardinia.vic.gov.au/images/cats_sml.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRUeB4aArDOntl48L6LFkyWtIf4nhH0YGYqmg&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT6fH4WcqPLntpPILC1Ag-_D7dkrljytz9iNg&usqp=CAU"]
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Here is your Cat Image!')
    embed.set_image(url=random.choice(choices))
    await ctx.send(embed=embed)

@client.command()
async def pun(ctx):
    choices = ["You can tune a guitar, but you can't tuna fish. Unless, of course, you play bass.", "Time flies like an arrow. Fruit flies like a banana.", "Hanging is too good for a man who makes puns; he should be drawn and quoted.", "I saw a documentary on how ships are kept together. Riveting!", "I Renamed my iPod The Titanic, so when I plug it in, it says “The Titanic is syncing.”", "I was wondering why the ball was getting bigger. Then it hit me", "Two windmills are standing in a wind farm. One asks, “What’s your favorite kind of music?” The other says, “I’m a big metal fan.”"]
    await ctx.send(random.choice(choices))

@client.command()
async def coinflip(ctx):
    choices = ["It is... Heads!", "It is... Tails!"]
    await ctx.send(random.choice(choices))

@image.command(pass_context=True)
async def redpanda(ctx):
    choices = ["https://cdn.vox-cdn.com/thumbor/1mxkqqttp-h6NTQ9fF6wbcXMcdg=/12x0:4907x3263/1400x1050/filters:focal(12x0:4907x3263):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/49388585/16071828377_85109fdee4_o.0.0.jpg", "https://static.scientificamerican.com/blogs/cache/file/8DB2EE5F-C195-4F57-9080554453E3E3C8.jpg", "https://www.nationalgeographic.com/content/dam/animals/thumbs/rights-exempt/mammals/r/red-panda_thumb.ngsversion.1485895956258.adapt.1900.1.JPG", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcThuWBqK4bsJVLgyjeCGLEBn1rOtb6boxDPpQ&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZAzAxVvW6_XWSPs7mkXIoiai53LGbEUpxJw&usqp=CAU", "https://img.huffingtonpost.com/asset/5cd3b3ab2100003000d403ac.jpeg?ops=1778_1000"]
    embed = discord.Embed(
        colour = discord.Colour.blue())
    embed.set_author(name='Here is your Red Panda!')
    embed.set_image(url=random.choice(choices))
    await ctx.send(embed=embed)

@client.command()
async def say(ctx, arg):
    await ctx.send(arg)
    
@client.command()
async def whydidyou(ctx, arg):
    await ctx.send(f'why did you {arg} me')
    
@image.command()
async def list(ctx):
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed=discord.Embed(title="Here is the list for the swirl image command")
    embed.set_author(name="Lava Image List")
    embed.add_field(name="List", value="`pokemon`, `cats`, `redpanda`, `LRImage`", inline=False)
    embed.set_footer(text="Lava 2020")
    await ctx.send(embed=embed)
    
@image.command()
async def dog(ctx):
    choices = ["https://cdn.mos.cms.futurecdn.net/QjuZKXnkLQgsYsL98uhL9X-1200-80.jpg", "https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg", "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*", "https://tenor.com/view/dog-joystick-funny-dog-xbox-funny-animals-gif-18411432"]
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed=discord.Embed(title="Here is your doggo!")
    embed.set_image(url=random.choice(choices))
    await ctx.send(embed=embed)


client.run('token')
