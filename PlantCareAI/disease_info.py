disease_info = {

# 🍅 TOMATO

"Tomato_Early_blight": {
    "description": "Early blight is one of the most common tomato diseases, caused by the fungus Alternaria solani. It typically starts on older, lower leaves as small brown spots with concentric rings, creating a 'target spot' pattern. As the disease progresses, leaves yellow, wither, and drop prematurely, reducing the plant's ability to photosynthesize and produce fruit.",
    "scientific_name": "Alternaria solani",
    "severity": "Medium",
    "hosts": "Tomato, Potato, Eggplant",
    "transmission": "Wind & Rain Splash",
    "humidity_risk": 75,
    "causes": [
        "Fungal spores overwinter in infected plant debris and soil from previous seasons.",
        "Warm temperatures (24-29°C) combined with high humidity or frequent rainfall.",
        "Overhead irrigation that keeps foliage wet for extended periods.",
        "Poor air circulation due to overcrowding of plants."
    ],
    "treatment": [
        "Remove infected leaves immediately and destroy them away from the garden.",
        "Apply chlorothalonil or copper-based fungicide at first sign of infection.",
        "Avoid overhead watering — use drip irrigation at the base of plants.",
        "Keep proper spacing between plants to improve air circulation."
    ],
    "prevention": [
        {"title": "Crop Rotation", "detail": "Rotate tomato planting locations every 2-3 years to break the disease cycle."},
        {"title": "Mulching", "detail": "Apply 2-3 inches of organic mulch to prevent soil-borne spores from splashing onto leaves."},
        {"title": "Resistant Varieties", "detail": "Choose tomato varieties bred for early blight resistance such as 'Mountain Magic' or 'Defiant'."},
        {"title": "Sanitation", "detail": "Remove all plant debris at end of season. Do not compost infected material."}
    ]
},

"Tomato_Late_blight": {
    "description": "Late blight is a devastating disease caused by the oomycete pathogen Phytophthora infestans, infamous for causing the Irish Potato Famine. It produces large, dark, water-soaked lesions on leaves and stems, often with white fungal growth on the undersides. Under humid conditions, it can destroy entire fields within days.",
    "scientific_name": "Phytophthora infestans",
    "severity": "Critical",
    "hosts": "Tomato, Potato",
    "transmission": "Wind-borne Spores",
    "humidity_risk": 90,
    "causes": [
        "Airborne sporangia spread rapidly over long distances during cool, wet weather.",
        "Temperatures between 10-25°C with relative humidity above 80% create ideal conditions.",
        "Infected seed potatoes or transplants introducing the pathogen to new areas.",
        "Overhead irrigation and prolonged leaf wetness accelerating spore germination."
    ],
    "treatment": [
        "Remove and destroy infected plants immediately — do not compost.",
        "Apply copper-based fungicides (Bordeaux mixture) to surrounding healthy foliage.",
        "Use systemic fungicides like mefenoxam for advanced infections.",
        "Improve air circulation by proper staking and pruning lower branches."
    ],
    "prevention": [
        {"title": "Plant Spacing", "detail": "Space plants 60-90cm apart to maximize air circulation and reduce humidity."},
        {"title": "Water Management", "detail": "Water at the base of plants early in the morning so foliage dries quickly."},
        {"title": "Resistant Cultivars", "detail": "Plant resistant varieties such as 'Mountain Merit' or 'Iron Lady'."},
        {"title": "Monitor Weather", "detail": "Apply preventive fungicides before periods of cool, wet weather."}
    ]
},

"Tomato_Leaf_Mold": {
    "description": "Leaf mold is caused by the fungus Passalora fulva (formerly Cladosporium fulvum). It thrives in conditions of high humidity and poor ventilation, making it particularly problematic in greenhouses. Symptoms include pale green to yellow spots on upper leaf surfaces with olive-green to grayish-purple velvety growth on the undersides.",
    "scientific_name": "Passalora fulva",
    "severity": "Medium",
    "hosts": "Tomato",
    "transmission": "Airborne Spores",
    "humidity_risk": 85,
    "causes": [
        "High relative humidity (above 85%) and temperatures between 22-25°C.",
        "Poor ventilation in greenhouses or tightly spaced outdoor plantings.",
        "Spores can survive on plant debris and greenhouse surfaces for extended periods.",
        "Overhead watering that increases leaf surface moisture."
    ],
    "treatment": [
        "Reduce humidity levels below 85% by improving ventilation.",
        "Remove and destroy infected leaves to reduce spore load.",
        "Apply fungicides containing chlorothalonil or mancozeb.",
        "Avoid wetting leaves during irrigation."
    ],
    "prevention": [
        {"title": "Ventilation", "detail": "Ensure adequate air flow by spacing plants and pruning lower leaves."},
        {"title": "Resistant Varieties", "detail": "Use varieties with Cf gene resistance when available."},
        {"title": "Humidity Control", "detail": "In greenhouses, use fans and vents to keep humidity below 80%."},
        {"title": "Drip Irrigation", "detail": "Water at soil level to avoid wetting foliage."}
    ]
},

"Tomato_Septoria_leaf_spot": {
    "description": "Septoria leaf spot is one of the most common and destructive diseases of tomato foliage, caused by the fungus Septoria lycopersici. It produces numerous small circular spots (1-3mm) with dark brown borders and tan or gray centers, often containing tiny black fruiting bodies (pycnidia). While it rarely kills the plant directly, severe defoliation reduces vigor and exposes fruit to sunscald.",
    "scientific_name": "Septoria lycopersici",
    "severity": "Medium",
    "hosts": "Tomato, Solanaceous",
    "transmission": "Water Splash",
    "humidity_risk": 82,
    "causes": [
        "Overwintering in infected plant debris from previous seasons.",
        "Prolonged periods of high humidity and temperatures between 15-27°C.",
        "Overhead irrigation or heavy rainfall facilitating spore splash from soil to leaves.",
        "Working among wet plants spreading spores on hands and tools."
    ],
    "treatment": [
        "Remove and destroy infected lower leaves at first sign of disease.",
        "Apply copper-based fungicides or bio-fungicides containing Bacillus subtilis.",
        "Use chlorothalonil-based fungicide for severe outbreaks.",
        "Avoid working with plants when foliage is wet."
    ],
    "prevention": [
        {"title": "Crop Rotation", "detail": "Wait 3 years before planting Solanaceous crops in the same area."},
        {"title": "Mulching", "detail": "Apply a layer of straw or plastic mulch to prevent soil-to-leaf splash."},
        {"title": "Air Circulation", "detail": "Properly stake and space plants to ensure rapid leaf drying."},
        {"title": "Clean Tools", "detail": "Disinfect pruning tools between plants to prevent spread."}
    ]
},

"Tomato_Spider_mites_Two_spotted_spider_mite": {
    "description": "Two-spotted spider mites (Tetranychus urticae) are tiny arachnids that feed on plant cells by piercing leaf tissue and sucking out contents. Infestations cause stippling (tiny yellow dots), bronzing, and eventual leaf drop. Fine webbing on the undersides of leaves is a telltale sign. They reproduce rapidly in hot, dry conditions and can devastate crops within weeks.",
    "scientific_name": "Tetranychus urticae",
    "severity": "High",
    "hosts": "Tomato, Beans, Strawberry, 200+ species",
    "transmission": "Wind & Contact",
    "humidity_risk": 30,
    "causes": [
        "Hot, dry conditions (above 30°C) accelerate mite reproduction dramatically.",
        "Overuse of broad-spectrum insecticides eliminating natural predators.",
        "Dusty conditions on leaf surfaces creating favorable microhabitats.",
        "Introduction via contaminated transplants or garden tools."
    ],
    "treatment": [
        "Spray plants with strong jet of water to physically remove mites and webbing.",
        "Apply neem oil or insecticidal soap, covering undersides of leaves thoroughly.",
        "Release predatory mites (Phytoseiulus persimilis) for biological control.",
        "Remove and destroy heavily infested leaves and plants."
    ],
    "prevention": [
        {"title": "Monitor Early", "detail": "Check undersides of leaves weekly with a hand lens, especially during hot weather."},
        {"title": "Maintain Humidity", "detail": "Regular misting discourages mite populations that prefer dry conditions."},
        {"title": "Avoid Pesticides", "detail": "Minimize broad-spectrum insecticide use to preserve natural predators."},
        {"title": "Quarantine", "detail": "Inspect new plants thoroughly before introducing to the garden."}
    ]
},

"Tomato_Target_Spot": {
    "description": "Target spot is caused by the fungus Corynespora cassiicola and produces distinctive brown lesions with concentric rings on leaves, stems, and fruit. Lesions start as small, water-soaked spots that enlarge and develop a target-like appearance. Severe infections can cause significant defoliation and reduce fruit quality and yield.",
    "scientific_name": "Corynespora cassiicola",
    "severity": "Medium",
    "hosts": "Tomato, Pepper, Cucumber",
    "transmission": "Rain Splash & Wind",
    "humidity_risk": 78,
    "causes": [
        "Warm temperatures (20-30°C) with prolonged periods of high humidity.",
        "Frequent rainfall or overhead irrigation keeping leaves wet.",
        "Dense plant canopies restricting air movement.",
        "Fungal spores surviving on infected crop debris between seasons."
    ],
    "treatment": [
        "Remove infected leaves and destroy them away from the garden.",
        "Apply fungicide spray containing azoxystrobin or chlorothalonil.",
        "Avoid overcrowding plants to improve air circulation.",
        "Keep field clean of plant debris."
    ],
    "prevention": [
        {"title": "Proper Spacing", "detail": "Plant tomatoes at recommended distances to allow air flow."},
        {"title": "Pruning", "detail": "Remove lower branches and suckers to improve ventilation."},
        {"title": "Clean Cultivation", "detail": "Remove all crop residue at end of season."},
        {"title": "Fungicide Schedule", "detail": "Begin preventive fungicide applications early in the growing season."}
    ]
},

"Tomato_Tomato_YellowLeaf_Curl_Virus": {
    "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is a devastating geminivirus transmitted by the sweetpotato whitefly (Bemisia tabaci). Infected plants exhibit severe upward curling and yellowing of leaves, stunted growth, flower drop, and dramatically reduced fruit production. Once infected, there is no cure — the plant remains a source of virus for whitefly transmission.",
    "scientific_name": "Begomovirus (TYLCV)",
    "severity": "Critical",
    "hosts": "Tomato, Pepper, Bean",
    "transmission": "Whitefly Vector",
    "humidity_risk": 65,
    "causes": [
        "Transmission by Bemisia tabaci (silverleaf whitefly) — acquires virus in minutes.",
        "High whitefly populations during warm seasons with temperatures above 25°C.",
        "Infected transplants introducing the virus to new growing areas.",
        "Proximity to other infected crops serving as virus reservoirs."
    ],
    "treatment": [
        "Remove and destroy infected plants immediately to reduce virus source.",
        "Control whitefly populations using yellow sticky traps and insecticidal soaps.",
        "Apply systemic insecticides (imidacloprid) to protect remaining healthy plants.",
        "Use reflective mulches to deter whiteflies from landing."
    ],
    "prevention": [
        {"title": "Resistant Seeds", "detail": "Plant TYLCV-resistant varieties such as 'Ty-1', 'Ty-2', or 'Ty-3' gene carriers."},
        {"title": "Physical Barriers", "detail": "Use fine-mesh insect netting or row covers to exclude whiteflies."},
        {"title": "Whitefly Management", "detail": "Monitor and control whitefly populations before they can transmit virus."},
        {"title": "Field Hygiene", "detail": "Remove volunteer tomato plants and weeds that harbor whiteflies."}
    ]
},

"Tomato_Tomato_mosaic_virus": {
    "description": "Tomato Mosaic Virus (ToMV) is a highly contagious tobamovirus that causes mottled light and dark green patterns on leaves, leaf distortion, stunted growth, and reduced fruit quality. The virus is extremely stable and can persist on contaminated surfaces, tools, and even tobacco products for years. It spreads primarily through mechanical contact.",
    "scientific_name": "Tobamovirus (ToMV)",
    "severity": "High",
    "hosts": "Tomato, Pepper, Tobacco",
    "transmission": "Mechanical Contact",
    "humidity_risk": 50,
    "causes": [
        "Mechanical transmission through contaminated hands, tools, and clothing.",
        "Infected seeds carrying the virus internally or on the seed coat.",
        "Contact with tobacco products contaminated with closely related Tobacco Mosaic Virus.",
        "Virus particles persisting on greenhouse surfaces and equipment."
    ],
    "treatment": [
        "Remove and destroy infected plants — there is no chemical cure for viruses.",
        "Disinfect all tools, stakes, and equipment with 10% bleach or trisodium phosphate.",
        "Wash hands thoroughly with soap before and after handling plants.",
        "Do not save seeds from infected plants."
    ],
    "prevention": [
        {"title": "Seed Treatment", "detail": "Use certified virus-free seeds or treat seeds with 10% trisodium phosphate."},
        {"title": "Hygiene", "detail": "Wash hands with milk or soap before handling plants — milk protein inactivates ToMV."},
        {"title": "Resistant Varieties", "detail": "Choose ToMV-resistant varieties carrying the Tm-2 resistance gene."},
        {"title": "No Smoking", "detail": "Avoid handling plants after using tobacco products to prevent TMV cross-contamination."}
    ]
},

"Tomato_healthy": {
    "description": "This tomato plant shows no signs of disease, pest damage, or nutrient deficiency. The leaves display uniform deep green coloration with proper turgor and no visible lesions, spots, or discoloration. The plant appears to be in excellent health with vigorous growth patterns consistent with optimal growing conditions.",
    "scientific_name": "Solanum lycopersicum",
    "severity": "None",
    "hosts": "N/A",
    "transmission": "N/A",
    "humidity_risk": 0,
    "causes": [],
    "treatment": [
        "Maintain consistent watering schedule — 1-2 inches per week.",
        "Apply balanced fertilizer (10-10-10) every 3-4 weeks during growing season.",
        "Continue regular monitoring for early signs of disease or pest activity.",
        "Keep garden area clean and free of debris."
    ],
    "prevention": [
        {"title": "Regular Monitoring", "detail": "Inspect plants weekly for any early signs of disease, pests, or nutrient issues."},
        {"title": "Proper Nutrition", "detail": "Maintain balanced fertilization and soil pH between 6.0-6.8."},
        {"title": "Water Management", "detail": "Water consistently at the base, avoiding overhead irrigation."},
        {"title": "Companion Planting", "detail": "Plant basil, marigolds, or nasturtiums nearby to deter pests naturally."}
    ]
},

"Tomato_Bacterial_spot": {
    "description": "Bacterial spot of tomato is caused by several species of Xanthomonas, primarily Xanthomonas vesicatoria. It produces small, dark, water-soaked lesions on leaves, stems, and fruit. Leaf spots are typically angular, dark brown to black, and may be surrounded by yellow halos. Severe infections cause extensive defoliation, reducing fruit yield and quality. Fruit lesions appear as dark, raised, scab-like spots.",
    "scientific_name": "Xanthomonas vesicatoria",
    "severity": "High",
    "hosts": "Tomato, Pepper",
    "transmission": "Rain Splash & Seeds",
    "humidity_risk": 80,
    "causes": [
        "Contaminated seeds introducing bacteria to new plantings.",
        "Warm temperatures (24-30°C) combined with frequent rain or overhead irrigation.",
        "Rain splash and wind-driven rain spreading bacteria rapidly through fields.",
        "Workers handling wet, infected plants spreading bacteria on hands and tools."
    ],
    "treatment": [
        "Remove and destroy severely infected leaves and plants to reduce inoculum.",
        "Apply copper-based bactericides (copper hydroxide) at regular 7-10 day intervals.",
        "Avoid overhead watering — use drip irrigation to reduce splash dispersal.",
        "Use copper + mancozeb tank mix for improved efficacy against resistant strains."
    ],
    "prevention": [
        {"title": "Certified Seed", "detail": "Use only certified disease-free seed or treat seeds with hot water (50°C for 25 minutes)."},
        {"title": "Crop Rotation", "detail": "Rotate away from tomatoes and peppers for at least 2-3 years."},
        {"title": "Avoid Wet Work", "detail": "Do not work among plants when foliage is wet to prevent bacterial spread."},
        {"title": "Resistant Cultivars", "detail": "Plant varieties with bacterial spot resistance when available."}
    ]
},


# 🌶️ PEPPER

"Pepper__bell___Bacterial_spot": {
    "description": "Bacterial spot of pepper is caused by several species of Xanthomonas bacteria. It produces small, dark, water-soaked lesions on leaves that may become angular and develop yellow halos. Severely affected leaves turn yellow and drop, exposing fruit to sunscald. Fruit lesions appear as raised, scab-like spots that reduce marketability.",
    "scientific_name": "Xanthomonas campestris pv. vesicatoria",
    "severity": "High",
    "hosts": "Pepper, Tomato",
    "transmission": "Rain Splash & Seeds",
    "humidity_risk": 80,
    "causes": [
        "Contaminated seeds serving as primary source of bacterial inoculum.",
        "Warm temperatures (24-30°C) combined with frequent rain or overhead irrigation.",
        "Rain splash and wind-driven rain spreading bacteria between plants.",
        "Workers handling wet plants can spread bacteria on hands and tools."
    ],
    "treatment": [
        "Remove and destroy infected leaves and heavily affected plants.",
        "Apply copper-based bactericides (copper hydroxide) at regular intervals.",
        "Avoid overhead watering to reduce splash dispersal of bacteria.",
        "Use streptomycin-based sprays for severe outbreaks (where permitted)."
    ],
    "prevention": [
        {"title": "Clean Seed", "detail": "Use certified disease-free seeds or treat seeds with hot water (50°C for 25 min)."},
        {"title": "Crop Rotation", "detail": "Rotate away from peppers and tomatoes for at least 2-3 years."},
        {"title": "Avoid Wet Work", "detail": "Do not work among plants when foliage is wet to prevent bacterial spread."},
        {"title": "Resistant Varieties", "detail": "Plant varieties with bacterial spot resistance genes (Bs1, Bs2, Bs3)."}
    ]
},

"Pepper__bell___healthy": {
    "description": "This bell pepper plant displays excellent health with no visible signs of disease, pest damage, or nutritional deficiency. Leaves show vibrant green coloration, proper shape, and good turgor pressure. The plant demonstrates vigorous vegetative growth consistent with optimal growing conditions and proper cultural management.",
    "scientific_name": "Capsicum annuum",
    "severity": "None",
    "hosts": "N/A",
    "transmission": "N/A",
    "humidity_risk": 0,
    "causes": [],
    "treatment": [
        "Maintain consistent watering to keep soil evenly moist but not waterlogged.",
        "Apply calcium-rich fertilizer to prevent blossom end rot.",
        "Continue regular monitoring for aphids, whiteflies, and other common pests.",
        "Harvest peppers regularly to encourage continued fruit production."
    ],
    "prevention": [
        {"title": "Consistent Watering", "detail": "Maintain even soil moisture to prevent stress and blossom end rot."},
        {"title": "Balanced Nutrition", "detail": "Feed with a fertilizer higher in phosphorus and potassium during fruiting."},
        {"title": "Pest Monitoring", "detail": "Scout for aphids and whiteflies weekly, especially on leaf undersides."},
        {"title": "Proper Spacing", "detail": "Space plants 45-60cm apart for optimal air circulation and light exposure."}
    ]
},


# 🥔 POTATO

"Potato_Early_blight": {
    "description": "Potato early blight, caused by Alternaria solani, produces characteristic concentric-ringed ('target') lesions on lower, older leaves first. The disease progresses upward as the season advances, causing significant defoliation that reduces tuber size and yield. Tuber infections appear as dark, sunken, circular lesions with raised borders.",
    "scientific_name": "Alternaria solani",
    "severity": "Medium",
    "hosts": "Potato, Tomato, Eggplant",
    "transmission": "Wind & Rain",
    "humidity_risk": 72,
    "causes": [
        "Fungal spores overwintering in soil and infected plant debris.",
        "Alternating wet and dry periods with temperatures between 20-30°C.",
        "Nutrient-stressed plants (especially nitrogen-deficient) are more susceptible.",
        "Extended periods of leaf wetness from dew, rain, or overhead irrigation."
    ],
    "treatment": [
        "Remove infected leaves and destroy them away from the planting area.",
        "Apply protectant fungicides such as chlorothalonil or mancozeb.",
        "Ensure adequate nitrogen fertilization to maintain plant vigor.",
        "Avoid overhead irrigation; water at soil level."
    ],
    "prevention": [
        {"title": "Crop Rotation", "detail": "Rotate with non-solanaceous crops for at least 3 years."},
        {"title": "Resistant Cultivars", "detail": "Select potato varieties with moderate early blight resistance."},
        {"title": "Proper Nutrition", "detail": "Maintain adequate nitrogen levels to reduce plant susceptibility."},
        {"title": "Harvest Timing", "detail": "Harvest tubers after vine death and allow skin to set before storage."}
    ]
},

"Potato_Late_blight": {
    "description": "Potato late blight is caused by the oomycete Phytophthora infestans — the same pathogen responsible for the Great Irish Famine (1845-1852). It produces rapidly expanding, water-soaked, dark green to brown lesions on leaves, often with a white fuzzy growth on the undersides during humid conditions. Infected tubers develop a reddish-brown, granular rot that extends into the flesh.",
    "scientific_name": "Phytophthora infestans",
    "severity": "Critical",
    "hosts": "Potato, Tomato",
    "transmission": "Wind-borne Spores",
    "humidity_risk": 92,
    "causes": [
        "Cool, wet conditions (10-20°C) with relative humidity above 90%.",
        "Airborne sporangia traveling long distances on wind currents.",
        "Infected seed potatoes serving as primary inoculum source.",
        "Dense canopy trapping moisture and creating ideal microclimate for infection."
    ],
    "treatment": [
        "Destroy all infected plants and tubers immediately — burn or bury deeply.",
        "Apply systemic fungicides (metalaxyl/mefenoxam) at first signs of disease.",
        "Copper-based fungicides provide protectant action on healthy tissue.",
        "Hill soil around stems to prevent spore wash-down to tubers."
    ],
    "prevention": [
        {"title": "Certified Seed", "detail": "Use only certified disease-free seed potatoes from reputable sources."},
        {"title": "Resistant Varieties", "detail": "Plant cultivars with late blight resistance genes (R-genes or field resistance)."},
        {"title": "Destroy Volunteers", "detail": "Eliminate volunteer potato plants and cull piles that harbor the pathogen."},
        {"title": "Forecasting", "detail": "Monitor weather-based blight forecasting systems and spray preventively."}
    ]
},

"Potato_healthy": {
    "description": "This potato plant exhibits excellent health with strong, upright stems and uniformly green, well-developed foliage. No signs of blight, viral infection, insect damage, or nutrient deficiency are present. The plant appears vigorous with good canopy development, indicating optimal growing conditions and proper cultural management.",
    "scientific_name": "Solanum tuberosum",
    "severity": "None",
    "hosts": "N/A",
    "transmission": "N/A",
    "humidity_risk": 0,
    "causes": [],
    "treatment": [
        "Maintain proper watering — potatoes need 1-2 inches of water per week.",
        "Hill soil around base of plants as they grow to protect developing tubers.",
        "Apply balanced fertilizer with emphasis on potassium for tuber development.",
        "Continue monitoring for Colorado potato beetles and aphids."
    ],
    "prevention": [
        {"title": "Hilling", "detail": "Regularly hill soil around stems to prevent tuber greening and protect from blight spores."},
        {"title": "Proper Drainage", "detail": "Ensure well-drained soil to prevent waterlogging and root diseases."},
        {"title": "Seed Quality", "detail": "Always use certified, disease-free seed potatoes."},
        {"title": "Harvest Care", "detail": "Wait for vines to die back, then harvest carefully to avoid skin damage."}
    ]
}

}