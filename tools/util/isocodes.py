#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# isocodes
#
# Copyright (C) 2011
#     Einar Uvsløkk, <einar.uvslokk@linux.com>
#
# isocodes is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# oya-invitationals is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

# ISO-639
languages = {
    "Afar" : "aa",
    "Abkhazian" : "ab",
    "Avestan" : "ae",
    "Afrikaans" : "af",
    "Akan" : "ak",
    "Amharic" : "am",
    "Aragonese" : "an",
    "Arabic" : "ar",
    "Assamese" : "as",
    "Avaric" : "av",
    "Aymara" : "ay",
    "Azerbaijani" : "az",
    "Bashkir" : "ba",
    "Belarusian" : "be",
    "Bulgarian" : "bg",
    "Bihari" : "bh",
    "Bislama" : "bi",
    "Bambara" : "bm",
    "Bengali" : "bn",
    "Bangla" : "bn",
    "Tibetan" : "bo",
    "Breton" : "br",
    "Bosnian" : "bs",
    "Catalan" : "ca",
    "Chechen" : "ce",
    "Chamorro" : "ch",
    "Corsican" : "co",
    "Cree" : "cr",
    "Czech" : "cs",
    "Church Slavic" : "cu",
    "Chuvash" : "cv",
    "Welsh" : "cy",
    "Danish" : "da",
    "German" : "de",
    "Divehi" : "dv",
    "Maldivian" : "dv",
    "Dzongkha" : "dz",
    "Bhutani" : "dz",
    "Éwé" : "ee",
    "Greek" : "el",
    "English" : "en",
    "Esperanto" : "eo",
    "Spanish" : "es",
    "Estonian" : "et",
    "Basque" : "eu",
    "Persian" : "fa",
    "Fulah" : "ff",
    "Finnish" : "fi",
    "Fijian" : "fj",
    "Fiji" : "fj",
    "Faroese" : "fo",
    "French" : "fr",
    "Western Frisian" : "fy",
    "Irish" : "ga",
    "Scottish Gaelic" : "gd",
    "Galician" : "gl",
    "Guarani" : "gn",
    "Gujarati" : "gu",
    "Manx" : "gv",
    "Hausa" : "ha",
    "Hebrew (formerly iw)" : "he",
    "Hindi" : "hi",
    "Hiri Motu" : "ho",
    "Croatian" : "hr",
    "Haitian" : "ht",
    "Haitian Creole" : "ht",
    "Hungarian" : "hu",
    "Armenian" : "hy",
    "Herero" : "hz",
    "Interlingua" : "ia",
    "Indonesian (formerly in)" : "id",
    "Interlingue" : "ie",
    "Occidental" : "ie",
    "Igbo" : "ig",
    "Sichuan Yi" : "ii",
    "Nuosu" : "ii",
    "Inupiak" : "ik",
    "Inupiaq" : "ik",
    "Ido" : "io",
    "Icelandic" : "is",
    "Italian" : "it",
    "Inuktitut" : "iu",
    "Japanese" : "ja",
    "Javanese" : "jv",
    "Georgian" : "ka",
    "Kongo" : "kg",
    "Kikuyu" : "ki",
    "Gikuyu" : "ki",
    "Kuanyama" : "kj",
    "Kwanyama" : "kj",
    "Kazakh" : "kk",
    "Kalaallisut" : "kl",
    "Greenlandic" : "kl",
    "Central Khmer" : "km",
    "Cambodian" : "km",
    "Kannada" : "kn",
    "Korean" : "ko",
    "Kanuri" : "kr",
    "Kashmiri" : "ks",
    "Kurdish" : "ku",
    "Komi" : "kv",
    "Cornish" : "kw",
    "Kirghiz" : "ky",
    "Latin" : "la",
    "Letzeburgesch" : "lb",
    "Luxembourgish" : "lb",
    "Ganda" : "lg",
    "Limburgish" : "li",
    "Limburger" : "li",
    "Limburgan" : "li",
    "Lingala" : "ln",
    "Lao" : "lo",
    "Laotian" : "lo",
    "Lithuanian" : "lt",
    "Luba-Katanga" : "lu",
    "Latvian" : "lv",
    "Lettish" : "lv",
    "Malagasy" : "mg",
    "Marshallese" : "mh",
    "Maori" : "mi",
    "Macedonian" : "mk",
    "Malayalam" : "ml",
    "Mongolian" : "mn",
    "Moldavian" : "mo",
    "Marathi" : "mr",
    "Malay" : "ms",
    "Maltese" : "mt",
    "Burmese" : "my",
    "Nauru" : "na",
    "Norwegian Bokmål" : "nb",
    "Ndebele, North" : "nd",
    "Nepali" : "ne",
    "Ndonga" : "ng",
    "Dutch" : "nl",
    "Norwegian Nynorsk" : "nn",
    "Norwegian" : "no",
    "Ndebele, South" : "nr",
    "Navajo" : "nv",
    "Navaho" : "nv",
    "Chichewa" : "ny",
    "Nyanja" : "ny",
    "Occitan" : "oc",
    "Provençal" : "oc",
    "Ojibwa" : "oj",
    "(Afan) Oromo" : "om",
    "Oriya" : "or",
    "Ossetian" : "os",
    "Ossetic" : "os",
    "Panjabi" : "pa",
    "Punjabi" : "pa",
    "Pali" : "pi",
    "Polish" : "pl",
    "Pashto" : "ps",
    "Pushto" : "ps",
    "Portuguese" : "pt",
    "Quechua" : "qu",
    "Romansh" : "rm",
    "Rundi" : "rn",
    "Kirundi" : "rn",
    "Romanian" : "ro",
    "Russian" : "ru",
    "Kinyarwanda" : "rw",
    "Sanskrit" : "sa",
    "Sardinian" : "sc",
    "Sindhi" : "sd",
    "Northern Sami" : "se",
    "Sango" : "sg",
    "Sangro" : "sg",
    "Sinhala" : "si",
    "Sinhalese" : "si",
    "Slovak" : "sk",
    "Slovenian" : "sl",
    "Samoan" : "sm",
    "Shona" : "sn",
    "Somali" : "so",
    "Albanian" : "sq",
    "Serbian" : "sr",
    "Swati" : "ss",
    "Siswati" : "ss",
    "Sesotho" : "st",
    "Sotho, Southern" : "st",
    "Sundanese" : "su",
    "Swedish" : "sv",
    "Swahili" : "sw",
    "Tamil" : "ta",
    "Telugu" : "te",
    "Tajik" : "tg",
    "Thai" : "th",
    "Tigrinya" : "ti",
    "Turkmen" : "tk",
    "Tagalog" : "tl",
    "Tswana" : "tn",
    "Setswana" : "tn",
    "Tonga" : "to",
    "Turkish" : "tr",
    "Tsonga" : "ts",
    "Tatar" : "tt",
    "Twi" : "tw",
    "Tahitian" : "ty",
    "Uighur" : "ug",
    "Ukrainian" : "uk",
    "Urdu" : "ur",
    "Uzbek" : "uz",
    "Venda" : "ve",
    "Vietnamese" : "vi",
    "Volapük" : "vo",
    "Volapuk" : "vo",
    "Walloon" : "wa",
    "Wolof" : "wo",
    "Xhosa" : "xh",
    "Yiddish (formerly ji)" : "yi",
    "Yoruba" : "yo",
    "Zhuang" : "za",
    "Chinese" : "zh",
    "Zulu" : "zu",
}

# ISO-3166
countries = {
    "Andorra" : "AD",
    "United Arab Emirates" : "AE",
    "Afghanistan" : "AF",
    "Antigua and Barbuda" : "AG",
    "Anguilla" : "AI",
    "Albania" : "AL",
    "Armenia" : "AM",
    "Netherlands Antilles" : "AN",
    "Angola" : "AO",
    "Antarctica" : "AQ",
    "Argentina" : "AR",
    "Samoa (American)" : "AS",
    "Austria" : "AT",
    "Australia" : "AU",
    "Aruba" : "AW",
    "Aaland Islands" : "AX",
    "Azerbaijan" : "AZ",
    "Bosnia and Herzegovina" : "BA",
    "Barbados" : "BB",
    "Bangladesh" : "BD",
    "Belgium" : "BE",
    "Burkina Faso" : "BF",
    "Bulgaria" : "BG",
    "Bahrain" : "BH",
    "Burundi" : "BI",
    "Benin" : "BJ",
    "Bermuda" : "BM",
    "Brunei" : "BN",
    "Bolivia" : "BO",
    "Brazil" : "BR",
    "Bahamas" : "BS",
    "Bhutan" : "BT",
    "Bouvet Island" : "BV",
    "Botswana" : "BW",
    "Belarus" : "BY",
    "Belize" : "BZ",
    "Canada" : "CA",
    "Cocos (Keeling) Islands" : "CC",
    "Congo (Dem. Rep.)" : "CD",
    "Central African Republic" : "CF",
    "Congo (Rep.)" : "CG",
    "Switzerland" : "CH",
    "Côte d'Ivoire" : "CI",
    "Cook Islands" : "CK",
    "Chile" : "CL",
    "Cameroon" : "CM",
    "China" : "CN",
    "Colombia" : "CO",
    "Costa Rica" : "CR",
    "Cuba" : "CU",
    "Cape Verde" : "CV",
    "Christmas Island" : "CX",
    "Cyprus" : "CY",
    "Czech Republic" : "CZ",
    "Germany" : "DE",
    "Djibouti" : "DJ",
    "Denmark" : "DK",
    "Dominica" : "DM",
    "Dominican Republic" : "DO",
    "Algeria" : "DZ",
    "Ecuador" : "EC",
    "Estonia" : "EE",
    "Egypt" : "EG",
    "Western Sahara" : "EH",
    "Eritrea" : "ER",
    "Spain" : "ES",
    "Ethiopia" : "ET",
    "Finland" : "FI",
    "Fiji" : "FJ",
    "Falkland Islands" : "FK",
    "Micronesia" : "FM",
    "Faeroe Islands" : "FO",
    "France" : "FR",
    "Gabon" : "GA",
    "Britain (United Kingdom)" : "GB",
    "Grenada" : "GD",
    "Georgia" : "GE",
    "French Guiana" : "GF",
    "Guernsey" : "GG",
    "Ghana" : "GH",
    "Gibraltar" : "GI",
    "Greenland" : "GL",
    "Gambia" : "GM",
    "Guinea" : "GN",
    "Guadeloupe" : "GP",
    "Equatorial Guinea" : "GQ",
    "Greece" : "GR",
    "South Georgia and the South Sandwich Islands" : "GS",
    "Guatemala" : "GT",
    "Guam" : "GU",
    "Guinea-Bissau" : "GW",
    "Guyana" : "GY",
    "Hong Kong" : "HK",
    "Heard Island and McDonald Islands" : "HM",
    "Honduras" : "HN",
    "Croatia" : "HR",
    "Haiti" : "HT",
    "Hungary" : "HU",
    "Indonesia" : "ID",
    "Ireland" : "IE",
    "Israel" : "IL",
    "Isle of Man" : "IM",
    "India" : "IN",
    "British Indian Ocean Territory" : "IO",
    "Iraq" : "IQ",
    "Iran" : "IR",
    "Iceland" : "IS",
    "Italy" : "IT",
    "Jersey" : "JE",
    "Jamaica" : "JM",
    "Jordan" : "JO",
    "Japan" : "JP",
    "Kenya" : "KE",
    "Kyrgyzstan" : "KG",
    "Cambodia" : "KH",
    "Kiribati" : "KI",
    "Comoros" : "KM",
    "St Kitts and Nevis" : "KN",
    "Korea (North)" : "KP",
    "Korea (South)" : "KR",
    "Kuwait" : "KW",
    "Cayman Islands" : "KY",
    "Kazakhstan" : "KZ",
    "Laos" : "LA",
    "Lebanon" : "LB",
    "St Lucia" : "LC",
    "Liechtenstein" : "LI",
    "Sri Lanka" : "LK",
    "Liberia" : "LR",
    "Lesotho" : "LS",
    "Lithuania" : "LT",
    "Luxembourg" : "LU",
    "Latvia" : "LV",
    "Libya" : "LY",
    "Morocco" : "MA",
    "Monaco" : "MC",
    "Moldova" : "MD",
    "Montenegro" : "ME",
    "Madagascar" : "MG",
    "Marshall Islands" : "MH",
    "Macedonia" : "MK",
    "Mali" : "ML",
    "Myanmar (Burma)" : "MM",
    "Mongolia" : "MN",
    "Macao" : "MO",
    "Northern Mariana Islands" : "MP",
    "Martinique" : "MQ",
    "Mauritania" : "MR",
    "Montserrat" : "MS",
    "Malta" : "MT",
    "Mauritius" : "MU",
    "Maldives" : "MV",
    "Malawi" : "MW",
    "Mexico" : "MX",
    "Malaysia" : "MY",
    "Mozambique" : "MZ",
    "Namibia" : "NA",
    "New Caledonia" : "NC",
    "Niger" : "NE",
    "Norfolk Island" : "NF",
    "Nigeria" : "NG",
    "Nicaragua" : "NI",
    "Netherlands" : "NL",
    "Norway" : "NO",
    "Nepal" : "NP",
    "Nauru" : "NR",
    "Niue" : "NU",
    "New Zealand" : "NZ",
    "Oman" : "OM",
    "Panama" : "PA",
    "Peru" : "PE",
    "French Polynesia" : "PF",
    "Papua New Guinea" : "PG",
    "Philippines" : "PH",
    "Pakistan" : "PK",
    "Poland" : "PL",
    "St Pierre and Miquelon" : "PM",
    "Pitcairn" : "PN",
    "Puerto Rico" : "PR",
    "Palestine" : "PS",
    "Portugal" : "PT",
    "Palau" : "PW",
    "Paraguay" : "PY",
    "Qatar" : "QA",
    "Reunion" : "RE",
    "Romania" : "RO",
    "Serbia" : "RS",
    "Russia" : "RU",
    "Rwanda" : "RW",
    "Saudi Arabia" : "SA",
    "Solomon Islands" : "SB",
    "Seychelles" : "SC",
    "Sudan" : "SD",
    "Sweden" : "SE",
    "Singapore" : "SG",
    "St Helena" : "SH",
    "Slovenia" : "SI",
    "Svalbard and Jan Mayen" : "SJ",
    "Slovakia" : "SK",
    "Sierra Leone" : "SL",
    "San Marino" : "SM",
    "Senegal" : "SN",
    "Somalia" : "SO",
    "Suriname" : "SR",
    "Sao Tome and Principe" : "ST",
    "El Salvador" : "SV",
    "Syria" : "SY",
    "Swaziland" : "SZ",
    "Turks and Caicos Islands" : "TC",
    "Chad" : "TD",
    "French Southern and Antarctic Lands" : "TF",
    "Togo" : "TG",
    "Thailand" : "TH",
    "Tajikistan" : "TJ",
    "Tokelau" : "TK",
    "Timor-Leste" : "TL",
    "Turkmenistan" : "TM",
    "Tunisia" : "TN",
    "Tonga" : "TO",
    "Turkey" : "TR",
    "Trinidad and Tobago" : "TT",
    "Tuvalu" : "TV",
    "Taiwan" : "TW",
    "Tanzania" : "TZ",
    "Ukraine" : "UA",
    "Uganda" : "UG",
    "US minor outlying islands" : "UM",
    "United States" : "US",
    "Uruguay" : "UY",
    "Uzbekistan" : "UZ",
    "Vatican City" : "VA",
    "St Vincent and the Grenadines" : "VC",
    "Venezuela" : "VE",
    "Virgin Islands (UK)" : "VG",
    "Virgin Islands (US)" : "VI",
    "Vietnam" : "VN",
    "Vanuatu" : "VU",
    "Wallis and Futuna" : "WF",
    "Samoa (Western)" : "WS",
    "Yemen" : "YE",
    "Mayotte" : "YT",
    "South Africa" : "ZA",
    "Zambia" : "ZM",
    "Zimbabwe" : "ZW",
}

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
