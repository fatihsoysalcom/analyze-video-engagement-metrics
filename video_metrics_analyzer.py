import math

def analyze_video_performance(video_data):
    """
    Analyzes video performance metrics beyond just total views,
    focusing on engagement and retention.
    """
    video_id = video_data.get('id', 'N/A')
    title = video_data.get('title', 'Untitled Video')
    total_views = video_data.get('total_views', 0)
    video_length_seconds = video_data.get('video_length_seconds', 1) # Avoid division by zero
    average_watch_time_seconds = video_data.get('average_watch_time_seconds', 0)
    likes = video_data.get('likes', 0)
    comments = video_data.get('comments', 0)
    shares = video_data.get('shares', 0)
    call_to_action_clicks = video_data.get('call_to_action_clicks', 0)

    print(f"\n--- Analyzing Video: '{title}' (ID: {video_id}) ---")
    print(f"Raw Metrics: Views={total_views}, Likes={likes}, Comments={comments}, Shares={shares}")
    print(f"Video Length: {video_length_seconds}s, Avg Watch Time: {average_watch_time_seconds:.2f}s")

    # --- Derived Metrics (Key to understanding true success) ---

    # Average Watch Percentage: How much of the video did viewers actually watch?
    # This is crucial for content quality and viewer retention, often overlooked by simple view counts.
    average_watch_percentage = (average_watch_time_seconds / video_length_seconds) * 100 if video_length_seconds > 0 else 0
    print(f"  -> Average Watch Percentage: {average_watch_percentage:.2f}%")

    # Engagement Rate: How interactive was the audience with the content?
    # Beyond just passive viewing, this shows active interest and community building.
    total_engagements = likes + comments + shares
    engagement_rate = (total_engagements / total_views) * 100 if total_views > 0 else 0
    print(f"  -> Engagement Rate (Likes+Comments+Shares per view): {engagement_rate:.2f}%")

    # Conversion Rate: Did the video lead to a desired action?
    # Important for business goals, e.g., clicks to a product page or subscription.
    conversion_rate = (call_to_action_clicks / total_views) * 100 if total_views > 0 else 0
    print(f"  -> Call-to-Action Conversion Rate: {conversion_rate:.2f}%")

    # --- Holistic Performance Assessment ---
    print("\nHolistic Performance Assessment:")

    # Interpret watch percentage
    if average_watch_percentage >= 70:
        print("  - Excellent Viewer Retention: Viewers are watching most of your video!")
    elif average_watch_percentage >= 40:
        print("  - Good Viewer Retention: Viewers are engaged for a significant portion.")
    else:
        print("  - Low Viewer Retention: Many viewers are dropping off early. Re-evaluate intro/pacing.")

    # Interpret engagement rate
    if engagement_rate >= 5:
        print("  - High Engagement: Your audience is actively interacting with the content.")
    elif engagement_rate >= 1:
        print("  - Moderate Engagement: Some interaction, but room to encourage more.")
    else:
        print("  - Low Engagement: Viewers are mostly passive. Consider calls to action or more interactive content.")

    # Interpret conversion rate
    if call_to_action_clicks > 0 and conversion_rate >= 0.5:
        print("  - Effective Call-to-Action: The video successfully drives desired actions.")
    elif call_to_action_clicks > 0:
        print("  - Some Call-to-Action Success: Driving some actions, but could be optimized.")
    else:
        print("  - No/Low Call-to-Action Success: The video isn't effectively driving desired actions.")

    # Overall Score (simple weighted average for demonstration)
    # Weights can be adjusted based on content goals
    retention_score = min(average_watch_percentage / 100, 1.0) * 0.4 # Max 40 points
    interaction_score = min(engagement_rate / 10, 1.0) * 0.3 # Max 30 points, assuming 10% is very high
    conversion_score = min(conversion_rate / 2, 1.0) * 0.3 # Max 30 points, assuming 2% is very high

    holistic_score = (retention_score + interaction_score + conversion_score) * 100
    print(f"\n  -> Overall Holistic Performance Score (out of 100): {holistic_score:.2f}")

    if holistic_score >= 75:
        print("  Verdict: Excellent performance! This video is highly successful across multiple dimensions.")
    elif holistic_score >= 50:
        print("  Verdict: Good performance! Solid engagement and retention, with areas for potential improvement.")
    else:
        print("  Verdict: Needs improvement. While views might be high, deeper engagement is lacking.")


if __name__ == "__main__":
    # Example 1: The "Scroll Trap" - High views, but low actual engagement
    # This scenario highlights why total views alone are insufficient.
    video_scroll_trap = {
        'id': 'V001',
        'title': 'Viral Clickbait Title!',
        'total_views': 1_500_000,
        'video_length_seconds': 60,
        'average_watch_time_seconds': 8, # Viewers only watch a small portion
        'likes': 15_000,
        'comments': 500,
        'shares': 100,
        'call_to_action_clicks': 50,
    }

    # Example 2: The "Engaged Audience" - Moderate views, but high quality engagement
    # This video, despite fewer views, demonstrates better content success.
    video_engaged_audience = {
        'id': 'V002',
        'title': 'Deep Dive into Python Async',
        'total_views': 80_000,
        'video_length_seconds': 600, # 10 minutes
        'average_watch_time_seconds': 450, # Viewers watch 75%
        'likes': 4_000,
        'comments': 300,
        'shares': 150,
        'call_to_action_clicks': 800, # Good conversion for a technical video
    }

    # Example 3: Low views, but very high quality engagement - Niche content
    # Demonstrates that for niche content, deeper metrics are even more critical.
    video_niche_success = {
        'id': 'V003',
        'title': 'Advanced Quantum Computing Concepts',
        'total_views': 5_000,
        'video_length_seconds': 1200, # 20 minutes
        'average_watch_time_seconds': 1000, # Viewers watch ~83%
        'likes': 500,
        'comments': 100,
        'shares': 50,
        'call_to_action_clicks': 100, # High conversion for a niche audience
    }

    analyze_video_performance(video_scroll_trap)
    analyze_video_performance(video_engaged_audience)
    analyze_video_performance(video_niche_success)