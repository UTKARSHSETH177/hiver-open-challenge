import json, argparse
from generator import generate_reply
from evaluate import evaluate_reply, hybrid_score
from judge import judge_reply

def run_pipeline():
    with open("data/sample_emails.json") as f:
        dataset = json.load(f)

    results = []
    for item in dataset:
        customer = item["customer"]
        ideal = item["ideal_reply"]

        generated = generate_reply(customer)
        scores = evaluate_reply(generated, ideal, customer)
        judge_scores = judge_reply(customer, generated, ideal)
        hybrid = hybrid_score(scores)

        print("\nCustomer:", customer)
        print("Generated Reply:", generated)
        print("Ideal Reply:", ideal)
        print("Scores:", scores)
        print("Hybrid Score:", hybrid)
        print("Judge Scores:", judge_scores)

        results.append({
            "customer": customer,
            "generated": generated,
            "scores": scores,
            "hybrid_score": hybrid,
            "judge_scores": judge_scores
        })

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    overall_semantic = sum(r["scores"]["semantic"] for r in results) / len(results)
    overall_hybrid = sum(r["hybrid_score"] for r in results) / len(results)

    print("\nOverall Semantic Accuracy:", round(overall_semantic, 3))
    print("Overall Hybrid Accuracy:", round(overall_hybrid, 3))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate", action="store_true", help="Generate dataset")
    parser.add_argument("--evaluate", action="store_true", help="Run evaluation")
    args = parser.parse_args()

    if args.generate:
        import dataset_generator
        dataset_generator.create_dataset()
        print("Dataset generated.")
    elif args.evaluate:
        run_pipeline()
    else:
        run_pipeline()
