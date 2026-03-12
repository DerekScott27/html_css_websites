{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN2nNPyvSzD7qdDD9Juraj7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DerekScott27/html_css_websites/blob/master/ufcStats-webScraper.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "XCJinXi4zlrP",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 315
        },
        "outputId": "76a7b43d-2c2d-453e-b617-19fd06fbb117"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Tom Aaron http://ufcstats.com/fighter-details/93fe7332d16c6ad9 0.00 0 0.00 0 0.00 0 0 0.0 \n",
            "Danny Abbadi http://ufcstats.com/fighter-details/15df64c02b6b0fde 3.29 38 4.41 57 0.00 0 77 0.0 \n",
            "Nariman Abbasov http://ufcstats.com/fighter-details/59a9d6dac61c2540 3.00 20 5.67 46 0.00 0 66 0.0 \n",
            "Darion Abbey http://ufcstats.com/fighter-details/4961467134abd8be 8.44 50 14.06 28 0.00 0 0 0.0 \n",
            "David Abbott http://ufcstats.com/fighter-details/b361180739bed4b0 1.35 30 3.55 38 1.07 33 66 0.0 \n",
            "Hamdy Abdelwahab http://ufcstats.com/fighter-details/3329d692aea4dc28 4.27 55 3.67 51 3.25 65 100 0.0 \n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_1118/1060524312.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     48\u001b[0m       \u001b[0;32mif\u001b[0m \u001b[0mstat\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'{firstName} {lastName} {link} {slpm} {str_acc} {sa_pm} {str_def} {td_avg} {td_acc} {td_def} {sub_avg} '\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 50\u001b[0;31m         \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     51\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     52\u001b[0m   \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ],
      "source": [
        "import requests\n",
        "import time\n",
        "import string\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "def clean_stat(value):\n",
        "  value = value.strip()\n",
        "  if value == '---' or value == \"\":\n",
        "     return None\n",
        "  return value\n",
        "\n",
        "for letter in string.ascii_lowercase:\n",
        "  url = f'http://ufcstats.com/statistics/fighters?char={letter}'\n",
        "  response = requests.get(url)\n",
        "  soup = BeautifulSoup(response.text, 'html.parser')\n",
        "  athlete = soup.select('tr.b-statistics__table-row')\n",
        "\n",
        "  for athlete in athlete:\n",
        "    fighter = athlete.select('td.b-statistics__table-col a')\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "    if fighter:\n",
        "      firstName = fighter[0].text\n",
        "      lastName = fighter[1].text\n",
        "      link = fighter[0].get('href')\n",
        "      fighter_page = requests.get(link)\n",
        "      fSoup = BeautifulSoup(fighter_page.text, 'html.parser')\n",
        "      stat = fSoup.select('div.b-list__info-box-left.clearfix')\n",
        "\n",
        "\n",
        "      for stat in stat:\n",
        "        attributes = stat.select('li.b-list__box-list-item')\n",
        "        slpm = clean_stat(attributes[0].text.strip().replace('SLpM:', '').strip())\n",
        "        str_acc = clean_stat(attributes[1].text.strip().replace('Str. Acc.:', '').strip().replace('%', \"\").strip())\n",
        "        sa_pm = clean_stat(attributes[2].text.strip().replace('SApM:', '').strip())\n",
        "        str_def = clean_stat(attributes[3].text.strip().replace('Str. Def:', '').strip().replace('%', \"\").strip())\n",
        "\n",
        "        li = attributes[5]\n",
        "        td_avg = clean_stat(li.text.replace(li.select_one('i').text, '').strip())\n",
        "\n",
        "        li = attributes[6]\n",
        "        td_acc = clean_stat(li.text.replace(li.select_one('i').text, '').strip().replace('%', \"\").strip())\n",
        "\n",
        "        li = attributes[7]\n",
        "        td_def = clean_stat(li.text.replace(li.select_one('i').text, '').strip().replace('%', \"\").strip())\n",
        "        sub_avg = clean_stat(attributes[8].text.strip().replace('Sub. Avg.:', '').strip())\n",
        "\n",
        "\n",
        "\n",
        "      if stat:\n",
        "        print(f'{firstName} {lastName} {link} {slpm} {str_acc} {sa_pm} {str_def} {td_avg} {td_acc} {td_def} {sub_avg} ')\n",
        "      time.sleep(1)\n",
        "\n",
        "    else:\n",
        "      print('No link found')\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}