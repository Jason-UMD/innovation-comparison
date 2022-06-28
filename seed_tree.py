from tech import Tech

# Source:
#       CRITICAL AND EMERGING TECHNOLOGIES LIST UPDATE
#       A Report by the FAST TRACK ACTION SUBCOMMITTEE ON CRITICAL AND EMERGING TECHNOLOGIES
#       of the NATIONAL SCIENCE AND TECHNOLOGY COUNCIL
tech_root = Tech('Critical Technologies', children=[
    Tech('Advanced Computing', children=[
        Tech('Supercomputing', seed_list=[]),
        Tech('Edge computing', seed_list=[]),
        Tech('Cloud computing', seed_list=[]),
        Tech('Data storage', seed_list=[]),
        Tech('Computing architectures', seed_list=[]),
        Tech('Data processing and analysis techniques', seed_list=[]),
    ]),
    Tech('Advanced Engineering Materials', children=[
        Tech('Materials by design and material genomics', seed_list=[]),
        Tech('Materials with new properties', seed_list=[]),
        Tech('Materials with substantial improvements to existing properties', seed_list=[]),
        Tech('Material property characterization and lifecycle assessment ', seed_list=[]),
    ]),
    Tech('Advanced Gas Turbine Engine Technologies', children=[
        Tech('Aerospace, maritime, and industrial development and production technologies', seed_list=[]),
        Tech('Full-authority digital engine control, hot-section manufacturing, and associated technologies', seed_list=[]),
    ]),
    Tech('Advanced Manufacturing', children=[
        Tech('Additive manufacturing', seed_list=[]),
        Tech('Clean, sustainable manufacturing', seed_list=[]),
        Tech('Smart manufacturing', seed_list=[]),
        Tech('Nanomanufacturing', seed_list=[]),
    ]),
    Tech('Advanced and Networked Sensing and Signature Management', children=[
        Tech('Payloads, sensors, and instruments', seed_list=[]),
        Tech('Sensor processing and data fusion', seed_list=[]),
        Tech('Adaptive optics', seed_list=[]),
        Tech('Remote sensing of the Earth', seed_list=[]),
        Tech('Signature management', seed_list=[]),
        Tech('Nuclear materials detection and characterization', seed_list=[]),
        Tech('Chemical weapons detection and characterization', seed_list=[]),
        Tech('Biological weapons detection and characterization', seed_list=[]),
        Tech('Emerging pathogens detection and characterization', seed_list=[]),
        Tech('Transportation-sector sensing', seed_list=[]),
        Tech('Security-sector sensing', seed_list=[]),
        Tech('Health-sector sensing', seed_list=[]),
        Tech('Energy-sector sensing', seed_list=[]),
        Tech('Building-sector sensing', seed_list=[]),
        Tech('Environmental-sector sensing', seed_list=[]),
    ]),
    Tech('Advanced Nuclear Energy Technologies ', children=[
        Tech('Nuclear energy systems ', seed_list=[]),
        Tech('Fusion energy', seed_list=[]),
        Tech('Space nuclear power and propulsion systems', seed_list=[]),
    ]),
    Tech('Artificial Intelligence (AI)', children=[
        Tech('Machine learning', seed_list=[]),
        Tech('Deep learning', seed_list=[]),
        Tech('Reinforcement learning', seed_list=[]),
        Tech('Sensory perception and recognition', seed_list=[]),
        Tech('Next-generation AI', seed_list=[]),
        Tech('Planning, reasoning, and decision making', seed_list=[]),
        Tech('Safe and/or secure AI', seed_list=[]),
    ]),
    Tech('Autonomous Systems and Robotics', children=[
        Tech('Surfaces', seed_list=[]),
        Tech('Air', seed_list=[]),
        Tech('Maritime', seed_list=[]),
        Tech('Space', seed_list=[]),
    ]),
    Tech('Biotechnologies', children=[
        Tech('Nucleic acid and protein synthesis', seed_list=[]),
        Tech('Genome and protein engineering including design tools', seed_list=[]),
        Tech('Multi-omics and other biometrology, bioinformatics, predictive modeling, and analytical tools for functional phenotypes', seed_list=[]),
        Tech('Engineering of multicellular systems', seed_list=[]),
        Tech('Engineering of viral and viral delivery systems', seed_list=[]),
        Tech('Biomanufacturing and bioprocessing technologies', seed_list=[]),
    ]),
    Tech('Communication and Networking Technologies', children=[
        Tech('Radio-frequency (RF) and mixed-signal circuits, antennas, filters, and components', seed_list=[]),
        Tech('Spectrum management technologies', seed_list=[]),
        Tech('Next-generation wireless networks, including 5G and 6G', seed_list=[]),
        Tech('Optical links and fiber technologies', seed_list=[]),
        Tech('Terrestrial/undersea cables', seed_list=[]),
        Tech('Satellite-based communications', seed_list=[]),
        Tech('Hardware, firmware, and software', seed_list=[]),
        Tech('Communications and network security', seed_list=[]),
        Tech('Mesh networks/infrastructure independent communication technologies', seed_list=[]),
    ]),
    Tech('Directed Energy', children=[
        Tech('Lasers', seed_list=[]),
        Tech('High-power microwaves', seed_list=[]),
        Tech('Particle beams', seed_list=[]),
    ]),
    Tech('Financial Technologies', children=[
        Tech('Distributed ledger technologies', seed_list=[]),
        Tech('Digital assets', seed_list=[]),
        Tech('Digital payment technologies', seed_list=[]),
        Tech('Digital identity infrastructure', seed_list=[]),
    ]),
    Tech('Human-Machine Interfaces ', children=[
        Tech('Augmented reality', seed_list=[]),
        Tech('Virtual reality', seed_list=[]),
        Tech('Brain-computer interfaces', seed_list=[]),
        Tech('Human-machine teaming', seed_list=[]),
    ]),
    Tech('Hypersonics', children=[
        Tech('Propulsion', seed_list=[]),
        Tech('Aerodynamics and control', seed_list=[]),
        Tech('Materials', seed_list=[]),
        Tech('Detection, tracking, and characterization', seed_list=[]),
        Tech('Defense', seed_list=[]),
    ]),
    Tech('Quantum Information Technologies', children=[
        Tech('Quantum computing', seed_list=[]),
        Tech('Materials, isotopes, and fabrication techniques for quantum devices', seed_list=[]),
        Tech('Post-quantum cryptography', seed_list=[]),
        Tech('Quantum sensing', seed_list=[]),
        Tech('Quantum networking', seed_list=[]),
    ]),
    Tech('Renewable Energy Generation and Storage', children=[
        Tech('Renewable generation', seed_list=[]),
        Tech('Renewable and sustainable fuels', seed_list=[]),
        Tech('Energy storage', seed_list=[]),
        Tech('Electric and hybrid engines', seed_list=[]),
        Tech('Batteries', seed_list=[]),
        Tech('Grid integration technologies', seed_list=[]),
        Tech('Energy-efficiency technologies', seed_list=[]),
    ]),
    Tech('Semiconductors and Microelectronics', children=[
        Tech('Design and electronic design automation tools', seed_list=[]),
        Tech('Manufacturing process technologies and manufacturing equipment', seed_list=[]),
        Tech('Beyond complementary metal-oxide-semiconductor (CMOS) technology', seed_list=[]),
        Tech('Heterogeneous integration and advanced packaging', seed_list=[]),
        Tech('Specialized/tailored   hardware   components   for   artificial   intelligence,   natural   and   hostile   radiation  environments,  RF  and  optical  components,  high-power  devices,  and  other  critical  applications', seed_list=[]),
        Tech('Novel materials for advanced microelectronics', seed_list=[]),
        Tech('Wide-bandgap and ultra-wide-bandgap technologies for power management, distribution, and transmission', seed_list=[]),
    ]),
    Tech('Space Technologies and Systems', children=[
        Tech('On-orbit servicing, assembly, and manufacturing', seed_list=[]),
        Tech('Commoditized satellite buses', seed_list=[]),
        Tech('Low-cost launch vehicles', seed_list=[]),
        Tech('Sensors for local and wide-field imaging', seed_list=[]),
        Tech('Space propulsion', seed_list=[]),
        Tech('Resilient positioning, navigation, and timing (PNT)', seed_list=[]),
        Tech('Cryogenic fluid management', seed_list=[]),
        Tech('Entry, descent, and landing', seed_list=[]),
    ]),
])