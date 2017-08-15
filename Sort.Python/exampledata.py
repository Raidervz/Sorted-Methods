from array import array
class exampledata(object):
    """description of class"""

    Data_1000 = [ 698, 685, 255, 700, 961, 984, 926, 931, 552, 783, 246, 307, 50, 689, 270, 514, 869, 958, 534, 163, 568, 223, 751, 697, 321, 302, 813, 694, 432, 405, 616, 427, 282, 118, 71, 948, 725, 980, 366, 283, 488, 140, 969, 822, 650, 978, 497, 896, 814, 23, 162, 43, 389, 819, 509, 691, 206, 964, 881, 536, 662, 578, 317, 444, 883, 437, 214, 169, 212, 453, 79, 753, 122, 387, 738, 579, 810, 30, 666, 94, 132, 583, 46, 398, 976, 801, 608, 501, 778, 12, 981, 544, 66, 701, 803, 196, 975, 112, 193, 443, 972, 602, 781, 49, 638, 996, 29, 712, 611, 91, 228, 237, 473, 96, 699, 428, 101, 831, 848, 757, 786, 138, 875, 309, 775, 442, 868, 936, 155, 576, 200, 596, 686, 907, 281, 85, 275, 164, 253, 267, 989, 81, 621, 244, 127, 494, 835, 340, 502, 454, 199, 827, 423, 990, 51, 987, 787, 203, 40, 927, 109, 539, 1, 520, 481, 88, 333, 823, 172, 218, 773, 137, 594, 355, 968, 970, 755, 724, 644, 3, 231, 750, 727, 546, 659, 612, 448, 271, 292, 677, 847, 487, 517, 986, 194, 61, 902, 456, 618, 627, 225, 406, 472, 525, 604, 220, 363, 38, 92, 587, 877, 75, 651, 359, 168, 221, 264, 912, 466, 524, 439, 374, 590, 412, 195, 742, 610, 817, 63, 538, 350, 873, 619, 531, 368, 388, 640, 305, 458, 434, 410, 669, 852, 789, 185, 433, 564, 105, 828, 11, 856, 294, 951, 493, 532, 909, 265, 337, 829, 216, 680, 661, 201, 22, 332, 921, 949, 506, 39, 744, 581, 451, 892, 347, 947, 625, 915, 84, 629, 826, 846, 274, 148, 474, 836, 354, 527, 561, 628, 186, 224, 526, 550, 286, 631, 285, 954, 402, 284, 114, 872, 2, 963, 119, 796, 500, 515, 762, 586, 278, 855, 361, 766, 866, 98, 108, 296, 776, 624, 33, 16, 403, 100, 791, 676, 999, 80, 166, 217, 841, 222, 982, 671, 937, 449, 720, 865, 174, 429, 131, 215, 408, 149, 143, 20, 381, 665, 718, 739, 709, 245, 150, 667, 117, 459, 325, 32, 1000, 974, 799, 192, 484, 145, 306, 623, 870, 373, 62, 794, 891, 854, 988, 495, 6, 182, 266, 863, 310, 279, 53, 67, 52, 48, 816, 938, 426, 730, 601, 175, 748, 290, 639, 106, 708, 468, 498, 10, 555, 809, 537, 957, 233, 251, 925, 991, 331, 695, 158, 656, 299, 394, 116, 521, 159, 483, 313, 295, 378, 272, 551, 729, 209, 435, 630, 678, 971, 804, 113, 256, 74, 276, 876, 470, 983, 151, 867, 950, 761, 977, 574, 553, 161, 346, 41, 15, 839, 956, 842, 998, 603, 336, 191, 707, 171, 457, 782, 510, 82, 234, 390, 731, 800, 772, 287, 18, 973, 479, 994, 249, 190, 726, 446, 658, 599, 655, 682, 102, 825, 834, 654, 189, 904, 966, 923, 243, 591, 570, 997, 425, 383, 58, 304, 44, 516, 522, 600, 397, 747, 376, 647, 734, 959, 681, 259, 211, 593, 45, 242, 606, 111, 445, 543, 861, 657, 298, 107, 763, 779, 219, 393, 716, 736, 914, 489, 664, 476, 693, 728, 385, 419, 399, 369, 696, 605, 965, 918, 411, 415, 900, 4, 144, 480, 862, 620, 24, 477, 503, 391, 314, 541, 204, 808, 257, 156, 475, 945, 330, 585, 136, 844, 210, 129, 139, 910, 675, 792, 153, 57, 268, 288, 652, 940, 207, 549, 540, 431, 706, 592, 17, 992, 352, 523, 953, 899, 486, 582, 607, 955, 469, 554, 14, 377, 183, 985, 188, 297, 584, 641, 133, 436, 653, 447, 597, 833, 424, 280, 450, 260, 505, 430, 952, 491, 34, 95, 897, 917, 922, 508, 884, 142, 460, 167, 805, 99, 252, 911, 420, 115, 702, 395, 471, 511, 87, 660, 277, 173, 878, 916, 344, 944, 202, 645, 69, 806, 464, 463, 54, 818, 547, 238, 893, 575, 913, 941, 455, 324, 311, 452, 740, 769, 334, 993, 362, 845, 703, 683, 802, 613, 499, 7, 577, 649, 301, 890, 213, 409, 933, 236, 533, 273, 467, 898, 8, 710, 401, 663, 357, 358, 688, 263, 614, 379, 821, 496, 979, 882, 90, 784, 530, 316, 197, 837, 920, 351, 930, 338, 83, 788, 47, 135, 312, 478, 152, 441, 622, 60, 895, 37, 905, 939, 556, 356, 248, 565, 637, 35, 178, 36, 125, 176, 65, 291, 507, 542, 737, 407, 254, 504, 438, 595, 832, 348, 229, 880, 797, 609, 241, 146, 461, 371, 668, 396, 760, 165, 187, 722, 752, 147, 72, 732, 184, 73, 181, 746, 888, 360, 894, 767, 721, 180, 318, 743, 535, 771, 559, 588, 908, 807, 943, 636, 580, 617, 93, 322, 513, 770, 230, 353, 528, 756, 780, 812, 840, 741, 719, 674, 315, 417, 21, 901, 820, 764, 995, 634, 768, 293, 545, 364, 765, 42, 864, 571, 320, 342, 759, 713, 335, 59, 572, 774, 679, 815, 329, 262, 860, 240, 626, 589, 343, 684, 227, 670, 308, 413, 55, 289, 28, 5, 529, 519, 9, 830, 485, 179, 208, 960, 416, 851, 386, 104, 672, 27, 97, 103, 123, 76, 319, 261, 879, 633, 56, 372, 404, 512, 300, 235, 567, 690, 857, 715, 704, 711, 490, 26, 934, 365, 919, 723, 563, 932, 745, 946, 714, 967, 560, 198, 134, 258, 492, 380, 646, 141, 327, 928, 811, 887, 110, 929, 13, 648, 566, 673, 367, 86, 226, 382, 121, 793, 130, 935, 850, 384, 375, 154, 635, 858, 942, 795, 19, 859, 642, 414, 160, 798, 239, 548, 370, 573, 598, 341, 303, 400, 906, 615, 128, 205, 89, 889, 31, 269, 339, 705, 247, 749, 177, 418, 790, 482, 824, 462, 558, 323, 70, 885, 903, 849, 422, 345, 843, 126, 326, 886, 962, 643, 758, 421, 735, 465, 785, 64, 250, 754, 232, 440, 77, 328, 68, 78, 717, 687, 853, 838, 170, 392, 733, 157, 924, 518, 569, 124, 874, 692, 557, 632, 25, 120, 777, 349, 871, 562 ]


