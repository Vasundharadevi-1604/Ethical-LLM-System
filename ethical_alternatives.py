# ethical_alternatives.py
# ---------------------------------------------------
# Domain-wise Ethical Alternatives Generator
# ---------------------------------------------------

def generate_ethical_alternatives(risk_domain: str = "General"):

    DOMAIN_ALTERNATIVES = {

        # ---------------------------------------------------
        # Violence / Physical Harm
        # ---------------------------------------------------
        "Violence": {
            "intro": (
                "⚠️ This request involves violence or physical harm and cannot be fulfilled."
            ),
            "bullets": [
                "Learn about the psychological and social causes of violence",
                "Understand conflict resolution and de-escalation techniques",
                "Explore laws and ethical frameworks governing use of force",
                "Study historical case studies focused on prevention and peace-building"
            ],
            "closing": (
                "I can help you explore this topic from a non-violent, educational perspective."
            )
        },

        # ---------------------------------------------------
        # Weapons / Explosives
        # ---------------------------------------------------
        "Weapons": {
            "intro": (
                "⚠️ Requests related to weapons or explosives are restricted for safety reasons."
            ),
            "bullets": [
                "Understand international laws on weapons control",
                "Learn about the physics of explosions at a high level (no construction details)",
                "Study the societal impact of weapons proliferation",
                "Explore careers in defense ethics, policy, or disarmament"
            ],
            "closing": (
                "Let me know if you'd like safe, theoretical, or policy-level information instead."
            )
        },

        # ---------------------------------------------------
        # Cybercrime / Hacking
        # ---------------------------------------------------
        "Cybercrime": {
            "intro": (
                "⚠️ This request involves hacking or cybercrime and cannot be supported."
            ),
            "bullets": [
                "Learn how cybersecurity systems protect networks",
                "Understand common cyber threats and how to defend against them",
                "Explore ethical hacking and penetration testing careers",
                "Study cybersecurity laws and digital forensics"
            ],
            "closing": (
                "I can help you learn cybersecurity in a legal and ethical way."
            )
        },

        # ---------------------------------------------------
        # Drugs / Illegal Substances
        # ---------------------------------------------------
        "Drugs": {
            "intro": (
                "⚠️ Requests involving illegal drugs or substance misuse are not allowed."
            ),
            "bullets": [
                "Learn about the medical effects of drugs on the human body",
                "Understand addiction science and rehabilitation methods",
                "Explore drug policy, law enforcement, and public health approaches",
                "Study harm-reduction strategies and awareness programs"
            ],
            "closing": (
                "I can provide educational or health-focused information if you'd like."
            )
        },

        # ---------------------------------------------------
        # Sexual / Adult Content
        # ---------------------------------------------------
        "Sexual Content": {
            "intro": (
                "⚠️ This request contains sexually explicit or age-restricted content."
            ),
            "bullets": [
                "Learn about human biology and reproduction in an educational context",
                "Understand consent, healthy relationships, and boundaries",
                "Explore psychology and sociology of human behavior",
                "Study legal frameworks around content regulation and safety"
            ],
            "closing": (
                "I can help with age-appropriate, educational information instead."
            )
        },

        # ---------------------------------------------------
        # Self-Harm / Suicide
        # ---------------------------------------------------
        "Self-Harm": {
            "intro": (
                "⚠️ This request relates to self-harm or suicide and cannot be addressed directly."
            ),
            "bullets": [
                "Learn about mental health awareness and emotional well-being",
                "Understand coping strategies and stress management techniques",
                "Explore psychology-based approaches to resilience",
                "Seek professional help or trusted support resources"
            ],
            "closing": (
                "If you're struggling, you are not alone. I can help you find support resources."
            )
        },

        # ---------------------------------------------------
        # Terrorism / Extremism
        # ---------------------------------------------------
        "Terrorism": {
            "intro": (
                "⚠️ Requests related to terrorism or extremist activities are strictly prohibited."
            ),
            "bullets": [
                "Study the historical causes of extremism",
                "Understand counter-terrorism strategies at a policy level",
                "Explore international security and peace studies",
                "Learn about social integration and radicalization prevention"
            ],
            "closing": (
                "I can help with academic or policy-based discussions on this topic."
            )
        },

        # ---------------------------------------------------
        # Fraud / Scams
        # ---------------------------------------------------
        "Fraud": {
            "intro": (
                "⚠️ Requests involving fraud, scams, or deception are not permitted."
            ),
            "bullets": [
                "Learn how common scams operate and how to avoid them",
                "Understand financial security and consumer protection laws",
                "Explore ethical business practices",
                "Study cybersecurity measures against online fraud"
            ],
            "closing": (
                "I can help you learn how to stay safe and protect yourself."
            )
        },

        # ---------------------------------------------------
        # Default / General Unsafe
        # ---------------------------------------------------
        "General": {
            "intro": (
                "⚠️ This request cannot be fulfilled due to ethical or safety concerns."
            ),
            "bullets": [
                "Explore the topic from a high-level theoretical perspective",
                "Understand ethical, legal, and societal implications",
                "Study real-world impacts and prevention strategies",
                "Focus on responsible and constructive learning approaches"
            ],
            "closing": (
                "Let me know how you'd like to explore this topic safely."
            )
        }
    }

    # Return domain-specific alternatives or default
    return DOMAIN_ALTERNATIVES.get(risk_domain, DOMAIN_ALTERNATIVES["General"])
