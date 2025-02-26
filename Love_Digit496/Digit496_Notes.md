# Digit 496 Notes:


## Installing homebrew :


1. Installing homebrew is for downloading java on your personal computer.
2. When needing to get homebrew you will open a new terminal on your computer then in a web browser look up this url : `https://brew.sh`
3. Once you have homebrew website open you should see a big header that says install homebrew and a line of terminal code below it `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`. You will need to copy the code into your terminal and this will start your launch process.
4. You will receive an error for sudo which represents "substitute user do" so to counter this error you will take the download code line for homebrew and add the word sudo before `sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` after running this line it will prompt you with asking for a password this is the password you use to login to you local computer.
5. Once you enter your password the terminal will the state "Checking for sudo access (which may request your password)... Don't run this as root!" aftering receiving this error you will then repaste that orginal homebrew install code.
6. After entering the original install code line the terminal will say "Checking for sudo access (which may request your password)... This script will install:" you may get asked you type in your computers password again but you will most likely not though if you do get asked for password just repeat past notes.
7. Once you get that installing note that the script will download your terminal will then run a bunch of code lines at the end of all those run lines the terminal will say `Next steps: Run these commands in your terminal to add Homebrew to your PATH: echo >> /Users/dannikalove/.zprofile echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/dannikalove/.zprofileeval "$(/opt/homebrew/bin/brew shellenv)" Run brew help to get started Further documentation: https://docs.brew.sh"`
8. You will need to be careful when running each one of those commands. You must run each line separately, 
* first run this command : `echo >> /Users/dannikalove/.zprofile` 
* next run this line : `echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/dannikalove/.zprofile` 
* lastly run this line : `eval "$(/opt/homebrew/bin/brew shellenv)"`


## Installing Java
1. To install java on your computer you must have homebrew installed first but if that is done you will type this command in the terminal to start the install process of java : `brew install openjdk`


## Setting up an alias
### Getting to zshell

1. `cd` 
1. `ls -lisa`
1. `nano .zshrc`

### Making alias

1. Example : `export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
alias github="cd /Users/dannikalove/Documents/Github"`

### Getting out of zshell 

1. 1. type : control X
1. 1. type : shift Y
1. 1. type : return/enter


## Installing Bat
1. Make sure to `cd` your terminal first
1. Type `brew install bat`
1. After installing at the ending of the install it will say where it was installed to. With collaboration from other testers we have found that bat will install to different location mine was `zsh completions have been installed to:  /opt/homebrew/share/zsh/site-functions` 


## Installing coffeepot

### When downloading coffeepot for mac users your computer will give you a malware error (it is not malware mac is just super careful) that you will need to bypass to continue the install process.
1. Go to your little apple icon in top left
1. Hit system settings
1. Then go to your privacy and security page
1. Once there scroll down to the bottom to the security section which will say something only the lines of "'coffeepot' was blocked to protect your mac" then have a 'allow anyway' or 'open anyway' button you will need to click. 

### These steps will allow you to continue the install process.
1. After installing coffeepot you will now need to create an alias.
1. First go to your home in your terminal by just typing `cd`
1. Next type `nano .zshrc` this is get you into your zshell.
1. Once in your shell you will make the alias here is mine note you will need to change the file paths to make sure it matches your computer and where everything is located : ` alias coffeepot='java -jar /Users/dannikalove/Documents/GitHub/coffeepot-3.2.7/coffeepot-3.2.7.jar'`
1. To save this you will need to exit the window like my instructions above to save this alias.
1. After getting out of the shell you will need to close the terminal to set the save for real.

### Now you will need to configure coffeepot to actually get to use it
1. First you will need to cd back to the home of your terminal.
1. We will be creating a system dot file. So you will type `touch .nineml.properties`
1. Next you will need to enter into that dot file by typeing into the terminal ` nano .nineml.properties`
1. Once in the dot file you will need to type : `graphviz=/opt/homebrew/bin/dot
ignore-trailing-whitespace=true
pretty-print=true
progress-bar=tty
assert-valid-xml-characters=true
assert-valid-xml-names=true
ignore-bom=true
normalize-line-endings=true
trailing-newline-on-output=true`
1. When you copy that in you may need to adjust the format of it if extra spaces are added.
1. Once you entered that code in you will need to exit the dot file to save it.
1. After leaving the dot file you can either close the terminal
1. You are finally able to start running coffeepot now. 

## Installing Markup Blitz
1. Follow the offical markup install instructions from the link : https://github.com/GuntherRademacher/markup-blitz
1. Next clone the markup blitz repo into your github folder using ` git clone https://github.com/GuntherRademacher/markup-blitz.git`
1. Next go to your markup directory by typing ` cd markup-blitz` to make sure it is running

### Making the Alias
1. Now you have to create an alias for markup in your z shell so first cd into your home directory using `cd`
1. Next nano into the shell by typign `nano .zshrc`
1. Once in the shell create the alias as such `alias blitz='java -jar /Users/dannikalove/Documents/GitHub/markup-blitz/build/libs/markup-blitz.jar'` (Note: your file path maybe different than mine)

### Test Running Blitz
1. To run Markup Blitz to process an ixml grammar and an input .txt file, use your new alias like this: `blitz filename.ixml filename.txt`

## Installing Calabash
1. Get it from here: https://github.com/xmlcalabash/xmlcalabash3/releases and look for the xmlcalabash zip file in the latest release
1. Unzip this if your computer does not do it for you and move it somewhere like your Github folder where it's easy to work with
1. Open your shell and navigate to your new xmlcalabash folder. For this to work we need to be able to use Java to execute the .jar file inside. Test if your Java installation works. This 'help' shell command will show you all the different commands available (edit this line to your calabash version): `java -jar xmlcalabash-app-3.0.0-alpha18.jar help`
### Graphviz install

1. First test if you have graphviz by entering this in your terminal: `dot -V`
1. Most likely you will probably need to install GraphViz, and you can do that by typing `brew install graphviz`

### CoffeeSacks install
1. This is needed for Calabash so first get the lastest version of CoffeeSacks from the repo, here: https://github.com/nineml/coffeesacks/releases
1. Now copy the CoffeeSacks jar file into your XML Calabash extra/ subdirectory folder

### Configuring Calabash
1. First you need to make the .xmlcalabash3 dot-file:
1. Navigate to your home directory by typing `cd` into your terminal
1. Next check where Homebrew installed graphviz. Double-check by navigating to see if Homebrew installed it in the default location: /opt/homebrew/bin/dot .
1. Next go back in your home directory with `cd`, we will now make a new file by typing `nano .xmlcalabash3` into your terminal 
1. This will create and open the new system file. Once this file is open you will need to type :
`<cc:xml-calabash xmlns:cc="https://xmlcalabash.com/ns/configuration">
    <cc:graphviz dot="/opt/homebrew/bin/dot"/>
 </cc:xml-calabash>`
 
### Creating an Alias for Calabash
1. First open up your .zshrc with `nano .zshrc`
1. You need the filepath of where you installed Calabash (I put mine in my GitHub folder)
1. Next create the alias this is what mine looks like ` alias calabash='/Users/dannikalove/Documents/GitHub/xmlcalabash-3.0.0-alpha18/xmlcalabash.sh --init:org.nineml.coffeesacks.RegisterCoffeeSacks'`

### Testing Calabash
1. To see if your installation is working navigate to your xmlcalabash repo and enter this command: calabash helloWorld.xpl. If your installation was successful you should see the following:
`=== result :: 1 :: file:/Users/dannikalove/Documents/GitHub/xmlcalabash-3.0.0-alpha20/helloWorld.xpl ===
 <helloWorld>This is XML Calabash version 3.0.0-alpha18.
 Share and enjoy!</helloWorld>`

## Installing Morgana
1. Download MorganaXProc-IIIse from Sourceforge and unzip the folder if your computer does not do it for you. I placed the folder into my GitHub folder to access it easier.

### Installing SchXslt
1. Find the latest version, and download the .zip file then unzip the folder if your computer does not do it for you.
1. Next move the folder into your Github folder

### Configuring Morgana
1. You will need to set up a morgana-config.xml configuration file.
1. To do this you will need to first `cd` into your home directory on your terminal
1. Next your gonna type `nano morgana-config.xml` once open you will need to paste this code in there: 
<morgana-config xmlns="http://www.xml-project.com/morganaxproc">
<!-- Relative paths are resolved by uri of this file -->

    <path_to_SchXSLT2_transpiler>/Users/eeb4/Documents/GitHub/schxslt2-1.3.4/transpile.xsl</path_to_SchXSLT2_transpiler>
	
    <XSLTValidationMode>LAX</XSLTValidationMode>

    <xslt-connector>Saxon12-3</xslt-connector>
    <xquery-connector>Saxon12-3</xquery-connector>
    <schematron-connector>schxslt2</schematron-connector>

    <xslt-config>/Users/eeb4/Documents/GitHub/xmlcalabash-3.0.0-alpha20/lib/Saxon-HE-12.5.jar</xslt-config>
    <xslt-config></xslt-config>
      <silent>true</silent>

<!--
<fo-connector>com.xml_project.morganaxproc3.fop2x.ApacheFOP2xConnector</fo-connector>
<fo-connector>com.xml_project.fosupport.AHFormatterV65.AHF65Connector</fo-connector>
-->

<!-- <ixml-connector>com.xml_project.morganaxproc3.ninemlConnector.NineMLConnector</ixml-connector> -->`
<ixml-connector>com.xml_project.morganaxproc3.markupblitzConnector.MarkupBlitzConnector</ixml-connector>

<!--
<mediatype-mapping>
	<map file-extension="123" media-type="application/xml" />
</mediatype-mapping>
-->
</morgana-config>

1. You will then need to edit this infomation with your file paths and these :
1. Change the <path_to_SchXSLT2_transpiler> element contents to your path to the transpile.xsl file in schxslt directory.
1. Change the <xslt-config> element contents to your path to Saxon-HE.

### Creating an Alias for Morgana
1. Time to make an alias for Morgana
1. First `cd` home then open up your .zshrc `nano .zshrc` my alias looks like this `alias morgana='/Users/dannikalove/Documents/GitHub/MorganaXProc-IIIse-1.5/Morgana.sh -config=/Users/eeb4/morgana-config.xml'` you will need to change this with your correct file path

### Installing CoffeeFilter and CoffeeGrinder
1. Download and install CoffeeFilter and CoffeeGrinder from https://github.com/nineml. (As usual I'm setting coffee stuff in my GitHub folder.)
1. Download the most recent CoffeeFilter, unzip it into your GitHub folder.
1. Download the most recent CoffeeGrinder, unzip it into your GitHub folder.

### More Morgana Configuration
1. Modifying Morgana.sh: 
1. First, navigate in your shell to where you saved the MorganaXproc-IIISe directory `ls`
1. Make sure it has a file named Morgana.sh inside with `ls -lisa` so that you can see its rwx (read-write-execute) properties. They probably look like this: -rw-r--r--@. We need to change it to make it executable.
1. Make Morgana.sh executable: Do this with `chmod +x Morgana.sh`
1. Now, we need to edit Morgana.sh by `nano Morgana.sh`
1. Once in you'll need to add and adjust the lines to match your file paths but this is what my sh has in it:

CURRENT_SCRIPT=$0
#CURRENT_SCRIPT="$(readlink -f "$0")"  #resolves symlinks on unix based systems (Does not work on BSD systems like MacOS)

#echo $0
MORGANA_HOME=$(dirname $CURRENT_SCRIPT)
MORGANA_LIB=$MORGANA_HOME/MorganaXProc-IIIse_lib/*

#Local customization
SAXON_JAR=/Users/dannikalove/Documents/Github/xmlcalabash-3.0.0-alpha18/lib/Saxon-HE-12.5.jar
COFFEEGRINDER_JAR=/Users/dannikalove/Documents/Github/coffeegrinder-3.2.7/CoffeeGrinder-3.2.7.jar
COFFEEFILTER_JAR=/Users/dannikalove/Documents/Github/coffeefilter-3.2.7/CoffeeFilter-3.2.7.jar
BLITZ_JAR=/Users/dannikalove/Documents/Github/markup-blitz/build/libs/markup-blitz.jar

#Settings for JAVA_AGENT: Only for Java 8 we have to use -javaagent.
JAVA_AGENT=""

JAVA_VER=$(java -version 2>&1 | sed -n ';s/.* version "\(.*\)\.\(.*\)\..*".*/\1\2/p;')

if [ $JAVA_VER = "18" ]
then
	JAVA_AGENT=-javaagent:$MORGANA_HOME/MorganaXProc-IIIse_lib/quasar-core-0.7.9.jar
fi

# All related jars are expected to be in $MORGANA_LIB. For externals jars: Add them to $CLASSPATH
CLASSPATH=$BLITZ_JAR:$COFFEEGRINDER_JAR:$COFFEEFILTER_JAR:$SAXON_JAR:$MORGANA_LIB:$MORGANA_HOME/MorganaXProc-IIIse.jar

java $JAVA_AGENT -cp $CLASSPATH com.xml_project.morganaxproc3.XProcEngine "$@"CURRENT_SCRIPT=$0
#CURRENT_SCRIPT="$(readlink -f "$0")"  #resolves symlinks on unix based systems (Does not work on BSD systems like MacOS)

#echo $0
MORGANA_HOME=$(dirname $CURRENT_SCRIPT)
MORGANA_LIB=$MORGANA_HOME/MorganaXProc-IIIse_lib/*

#Settings for JAVA_AGENT: Only for Java 8 we have to use -javaagent.
JAVA_AGENT=""

JAVA_VER=$(java -version 2>&1 | sed -n ';s/.* version "\(.*\)\.\(.*\)\..*".*/\1\2/p;')

if [ $JAVA_VER = "18" ]
then
	JAVA_AGENT=-javaagent:$MORGANA_HOME/MorganaXProc-IIIse_lib/quasar-core-0.7.9.jar
fi

# All related jars are expected to be in $MORGANA_LIB. For externals jars: Add them to $CLASSPATH
CLASSPATH=$MORGANA_LIB:$MORGANA_HOME/MorganaXProc-IIIse.jar

java $JAVA_AGENT -cp $CLASSPATH com.xml_project.morganaxproc3.XProcEngine "$@"

### Testing Morgana
1. To "smoke test" Morgana to see if it is properly installed, navigate to your Morgana repo and enter morgana pipeline.xpl. If your installation was successful, you will see the following:
 `$ morgana pipeline.xpl
 Hello world. This is an XProc 3.0 pipeline running.`

# Congrats you made it through the installations!!
