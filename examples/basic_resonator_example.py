"""
basic_resonator_example.py

Simple demonstration of the open-source MasterSLWSolver
Shows only the publicly released features:
- Coherence scoring
- Material optimisation
- Standing-wave / Vastu resonance scoring
- Basic resonator optimisation

License: MIT
Author: Abhishek Rathi
Date: April 2026
"""

from MasterSLWSolver import MasterSLWSolver

def main():
    print("=== ATOE Open Core - Basic Resonator Example ===\n")
    solver = MasterSLWSolver()

    # 1. Coherence Scoring (harmonic matching)
    print("1. Coherence Score between two frequencies")
    score = solver.calculate_coherence_score(88e6, 176e6)   # 88 MHz and its 2nd harmonic
    print(f"   88 MHz ↔ 176 MHz  →  Coherence Score: {score:.4f} (1.0 = perfect lock)\n")

    # 2. Material Science Optimiser
    print("2. Material Optimisation for 88 MHz resonator")
    result = solver.optimise_material("copper_graphite", 88e6)
    print(f"   Current material : {result['current_material']}")
    print(f"   Current Q-factor : {result['current_q_factor']}")
    print("   Suggested better materials:")
    for sug in result['suggested_materials']:
        print(f"     → {sug['material']:15} | Q = {sug['q_factor']} | +{sug['improvement_percent']}%")
    print()

    # 3. Standing Wave / Vastu Resonance Scoring
    print("3. Standing Wave Score for Golden-Ratio Cylinder (88 MHz)")
    score_data = solver.calculate_standing_wave_score(
        geometry_type="cylinder",
        dimensions=(0.62, 0.384),      # height = 0.62 m, diameter = 0.384 m
        frequency_hz=88e6
    )
    print(f"   Geometry          : {score_data['geometry']}")
    print(f"   Dimensions        : {score_data['dimensions_m']} m")
    print(f"   Coherence Score   : {score_data['coherence_score']}")
    print(f"   Recommendation    : {score_data['recommendation']}\n")

    # 4. Basic Resonator Optimisation
    print("4. Full Resonator Optimisation (200 MHz example)")
    opt = solver.optimise_resonator(
        geometry="golden_ratio_cylinder",
        target_frequency_hz=200e6,
        material="copper_graphite"
    )
    print(f"   Geometry          : {opt['geometry']}")
    print(f"   Target Frequency  : {opt['target_frequency_hz']/1e6:.1f} MHz")
    print(f"   Coherence Score   : {opt['coherence_score']}")
    if opt['material_recommendation']:
        print(f"   Recommended Material : {opt['material_recommendation']['material']}")
    print(f"   Note              : {opt['note']}")

    print("\n✅ Example completed successfully.")
    print("   These are the open-source modules only.")
    print("   Advanced patented features are not included.")


if __name__ == "__main__":
    main()
