import os
import re

# The Standard Footer & Floating CTA content
FOOTER_CONTENT = """    <!-- Footer -->
    <footer class="bg-slate-950 text-slate-400 py-16 border-t border-slate-900">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">
                <div>
                    <a href="/" class="block mb-6">
                        <img src="/images/mil-spec roofing logo.png" alt="Mil-Spec Roofing Logo"
                            class="h-16 w-auto object-contain opacity-90" />
                    </a>
                    <p class="text-sm leading-relaxed mb-6">
                        Veteran-owned, faith-based roofing solutions built with precision, integrity, and dependable
                        durability.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="hover:text-blue-500 transition-colors"><i data-lucide="facebook"
                                class="h-5 w-5"></i></a>
                        <a href="#" class="hover:text-blue-500 transition-colors"><i data-lucide="twitter"
                                class="h-5 w-5"></i></a>
                        <a href="#" class="hover:text-blue-500 transition-colors"><i data-lucide="instagram"
                                class="h-5 w-5"></i></a>
                        <a href="#" class="hover:text-blue-500 transition-colors"><i data-lucide="linkedin"
                                class="h-5 w-5"></i></a>
                    </div>
                </div>

                <div>
                    <h4 class="text-white font-bold uppercase tracking-wider mb-6">Company</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="/about-us/" class="hover:text-white transition-colors">About Us</a></li>
                        <li><a href="/faq/" class="hover:text-white transition-colors">FAQ</a></li>
                        <li><a href="/contact-us/" class="hover:text-white transition-colors">Contact</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold uppercase tracking-wider mb-6">Services</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="/services/residential-roofing/"
                                class="hover:text-white transition-colors">Residential
                                Roofing</a></li>
                        <li><a href="/services/commercial-roofing/"
                                class="hover:text-white transition-colors">Commercial Roofing</a>
                        </li>
                        <li><a href="/services/roof-repair/" class="hover:text-white transition-colors">Roof Repair</a>
                        </li>
                        <li><a href="/services/roof-replacement/" class="hover:text-white transition-colors">Roof
                                Replacement</a>
                        </li>
                        <li><a href="/services/roof-inspection/" class="hover:text-white transition-colors">Roof
                                Inspection</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold uppercase tracking-wider mb-6">Contact</h4>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-center"><i data-lucide="phone" class="h-4 w-4 mr-2 text-blue-500"></i>
                            281-813-5925
                        </li>
                        <li class="flex items-center"><i data-lucide="mail" class="h-4 w-4 mr-2 text-blue-500"></i>
                            info@mil-specroofing.com</li>
                        <li class="flex items-start"><i data-lucide="map-pin"
                                class="h-4 w-4 mr-2 mt-1 text-blue-500"></i>
                            <div>Service Area<br>Webster, TX & Greater Houston</div></li>
                    </ul>
                </div>
            </div>

            <div class="border-t border-slate-900 pt-8 flex flex-col md:flex-row justify-between items-center text-xs">
                <p>&copy; 2024 Mil-Spec Roofing & Construction. All rights reserved.</p>
                <p class="mt-2 md:mt-0">Built to protect what matters most.</p>
            </div>
        </div>
    </footer>

    <!-- Floating CTA -->
    <a href="/contact-us/"
        class="fixed bottom-6 right-6 z-50 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 md:py-4 md:px-8 rounded-full shadow-2xl transition-all transform hover:scale-105 flex items-center gap-3 uppercase tracking-wider border-2 border-white/20 backdrop-blur-sm group">
        <i data-lucide="clipboard-check" class="h-5 w-5 md:h-6 md:w-6 group-hover:animate-pulse"></i>
        <span class="text-xs md:text-base whitespace-nowrap">Get Free Estimate</span>
    </a>
"""

def update_footer(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find existing footer (greedy to capture everything from <footer to </footer>)
        # We also look for the floating CTA if it exists near the footer
        
        # Strategy:
        # 1. Remove existing footer if present.
        # 2. Remove existing floating CTA if present.
        # 3. Insert new block before <script src="/script.js"> OR </body>
        
        # Remove existing footer
        content = re.sub(r'<!-- Footer.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<footer.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)

        # Remove existing floating CTA (pattern matching generic "fixed bottom-6" or similar structure or just the extraction)
        # Being safer: Match the specific Floating CTA comment block if it exists
        content = re.sub(r'<!-- Floating CTA.*?</a>', '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # Clean up any multiple newlines left behind
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

        # Insert new footer
        # Try to insert before the main script tag
        if '<script src="/script.js"' in content:
            parts = content.split('<script src="/script.js"')
            new_content = parts[0] + "\n" + FOOTER_CONTENT + "\n    <script src=\"/script.js\"" + parts[1]
        elif '</body>' in content:
             parts = content.split('</body>')
             new_content = parts[0] + "\n" + FOOTER_CONTENT + "\n</body>" + parts[1]
        else:
            new_content = content + "\n" + FOOTER_CONTENT

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"Updated: {filepath}")

    except Exception as e:
        print(f"Failed to update {filepath}: {e}")

root_dir = "."
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):
            # Skip node_modules or .git if they exist (though not expected here)
            if ".git" in dirpath or "node_modules" in dirpath:
                continue
            
            filepath = os.path.join(dirpath, filename)
            update_footer(filepath)
