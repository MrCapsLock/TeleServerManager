#!/usr/bin/env bash

function main {
    CreateDB;
    getToken;

    createAdmin_='Y';
    createAdmin='';
    while [ "$createAdmin" != "y" ] && [ "$createAdmin" != "n" ] && [ "$createAdmin" != "Y" ] && [ "$createAdmin" != "N" ]
    do
      read -p "Do you want to Create Admin? (Y|n) " createAdmin__;
      createAdmin=${createAdmin__:-$createAdmin_};
    done
    if [ "$createAdmin" ==  "y" ] || [ "$createAdmin" ==  "Y" ];then
      CreateAdmin;
    fi
}
# ------------------------------------------------------------------------------------------------------
function getToken {
    echo 'what is your bot token? (use @BotFather if you dont have one)'
    read token

    tokenCheck_='Y';
    tokenCheck='';
    while [ "$tokenCheck" != "y" ] && [ "$tokenCheck" != "Y" ]
    do
      read -p "are you sure ? (your token is = $token ) (Y|n) " tokenCheck__;
      tokenCheck=${tokenCheck__:-$tokenCheck_};
    done
    sed -i "s/YOUR_TOKEN/$token/g" config.ini
    if [ $? -eq 0 ] ;then
        echo "----------------"
        echo "OK--> Token Replaced"
        echo "----------------"
    else
        echo "XX--> Cant Replace Token !"
        echo "----------------"
        exit
    fi

}
# ------------------------------------------------------------------------------------------------------
function CreateDB {
    # Create DB With sql file!
    cat bot/db.sql | sqlite3 database.db
    if [ $? -eq 0 ] ;then
        echo "----------------"
        echo "OK--> DB Created."
        echo "----------------"
    else
        echo "XX--> Cant Create DB !"
        echo "----------------"
        exit
    fi

}
# ------------------------------------------------------------------------------------------------------
function CreateAdmin {
    echo "----------------"
    echo 'What is your id? (use @userinfobot if you dont know whats yours)'
    read adminId;
    sqlite3 database.db "insert into users values(\"$adminId\");";
    if [ $? -eq 0 ] ;then
        echo "----------------"
        echo "OK--> Admin Added."
        echo "----------------"
    else
        echo "XX--> Cant Add Admin !"
        echo "----------------"
        exit
    fi
}


# ------------------------------------------------------------------------------------------------------

main


