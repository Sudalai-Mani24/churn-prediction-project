SHAP BASED RETENTION STRATEGIES INSIGHTS:


The SHAP summary plot and feature impact analysis provide deep insights into the key drivers of churn behavior in the user base. The following retention strategies are grounded in these interpretable machine learning insights:

TOP FEATURES INFLUENCING CHURN (Based on SHAP Values)
*Churn Risk Score
Observation: Higher churn risk scores are the most significant contributors to churn.
Strategy: Proactively target users with high churn risk scores using personalized retention campaigns (e.g., loyalty rewards, special offers, or customer satisfaction surveys).

*Minimum Daily Minutes
Observation: Lower minimum daily engagement correlates strongly with churn.
Strategy: Encourage consistent usage through nudges like “streak” badges, watch recommendations, or gamified incentives to maintain daily interaction.

*Maximum Days Inactive
Observation: More days of inactivity drastically increase churn probability.
Strategy: Trigger re-engagement workflows such as push notifications, reminder emails, or app-exclusive content when inactivity exceeds specific thresholds.

*Customer Support Calls
Observation: High interaction with support suggests dissatisfaction or unresolved issues.
Strategy: Improve issue resolution speed and analyze frequent complaint topics to reduce customer frustration. Follow up with feedback forms or goodwill gestures for high-contact users.

*Engagement Score
Observation: Lower engagement scores (less time spent weekly) are tied to higher churn.
Strategy: Use personalized content recommendations and in-app banners to increase engagement levels. Highlight trending or newly added shows based on individual preferences.

*Subscription Tenure
Observation: Longer tenure reduces churn likelihood.
Strategy: Offer exclusive perks (e.g., discounts, anniversary gifts, or early access) to long-term users as a gesture of appreciation to reinforce loyalty.

*Weekly Mins Watched
Observation: Higher weekly watch time reduces churn risk.
Strategy: Provide tailored watchlists, binge-worthy content series, or interactive content to keep users invested for longer durations each week.

👤 Age Group Dynamics
*Users < 30 Years:
Insight: Higher SHAP values → greater churn risk.
Strategy: This age group may be less brand-loyal. Engage them with dynamic content, student discounts, and social sharing features to increase stickiness.

*Users Aged 35–45:
Insight: SHAP values approach zero → churn risk stabilizes.
Strategy: Maintain retention through value consistency, family content, or bundled service options (e.g., multiple screens).

*Users > 50 Years:
Insight: Slight increase in churn risk again.
Strategy: Simplify the UI/UX, offer tech support assistance, and promote genres of interest (e.g., documentaries, regional shows).

**Cross-Feature Insight: Age vs Tenure
Observation: Users with longer tenure (pink SHAP dots) exhibit lower churn across all age groups.
Strategy: Develop age-specific loyalty programs that reward long-term engagement, and identify short-tenure users (blue SHAP dots) for early intervention and onboarding optimization.

ACTIONABLE SUMMARY:

| Feature                  | Insight                       | Retention Tactic                    |
| ------------------------ | ----------------------------- | ----------------------------------- |
| `churn_risk_score`       | Higher score → high churn     | Personalized retention offers       |
| `minimum_daily_mins`     | Lower mins → low engagement   | Daily activity incentives           |
| `maximum_days_inactive`  | More inactive days → churn    | Timely re-engagement nudges         |
| `customer_support_calls` | More calls → user frustration | Speedy resolution + feedback loop   |
| `engagement_score`       | Lower score → churn           | Personalized recommendations        |
| `subscription_tenure`    | Longer tenure → retention     | Loyalty rewards for long-term users |
| `weekly_mins_watched`    | Higher time → retention       | Promote binge-worthy content        |
