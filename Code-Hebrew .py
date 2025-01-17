import pandas as pd
from collections import Counter
import string

# Read the CSV file into a pandas DataFrame
file_path = 'C:\\Users\\shake\\Desktop\\MSC- Data Science\\Thesis\\Tables\\Agancies Data-CrowdTangle\\ISA2.csv'
data = pd.read_csv(file_path, dtype={'Message': str}, low_memory=False,encoding='utf-8')

# Function to count word frequency in a text
def count_words(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    # Count word frequency
    word_count = Counter(text)
    return word_count

 # Define keywords for each field
international_relations_keywords = ['דיפלומטיה', 'מדיניות חוץ', 'שיתוף פעולה בינלאומי', 'עניינים גלובליים', 'כוונה', 'הצהרה', 'כוונה אסטרטגית',
     'דיפלומט', 'שגריר', 'אמנה', 'פסגה', 'שגרירות',
     'או"ם', 'האומות המאוחדות', 'שמירה על שלום', 'מנהיגי עולם', 'יחסים דו-צדדיים', 'הסכם', 'חתימה', 'שותפות אסטרטגית', 'ראש הממשלה',
     'גיאופוליטיקה', 'ארגונים בינלאומיים', 'מועצת ביטחון', 'רב-צדדיות','סוכנויות חלל בינלאומיות',
     'שר חוץ', 'פרוטוקול', 'משימה דיפלומטית', 'דיאלוג בינלאומי', 'שנה טובה',
     'יישוב סכסוכים', 'תקשורת בין-תרבותית', 'הסכמי סחר', 'ממשל גלובלי',
     'אמנות בינלאומיות', 'יחסים דיפלומטיים', 'ועידות בינלאומיות', 'דיפלומטיה כלכלית',
     'חילופי תרבות', 'בריתות אסטרטגיות', 'משא ומתן לשלום', 'ענייני חוץ', 'ניתוח מדיניות', 'סוכנות החלל',
     'ענייני עולם', 'דו קיום', 'חיל דיפלומטי', 'חסינות דיפלומטית', 'נוף גיאופוליטי',
     'סיוע חוץ', 'שיתוף פעולה אזורי', 'קשרים דיפלומטיים', 'פסגות בינלאומיות', 'יציבות אזורית', 'וועדת משנה מדעית וטכנית', 'האומות המאוחדות', 'שימושים שלווים בחלל החיצון','COPUOS',' משאבי שטח',
     'פרוטוקול דיפלומטי', 'פוליטיקה בינלאומית', 'יחסים חוצי גבולות', 'חוק בינלאומי',
     'קהילה דיפלומטית', 'סחר חוץ', 'יחסים בין-ממשלתיים', 'דיפלומטיה ציבורית',
     'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'משימות דיפלומטיות', 'מוסכמות בינלאומיות', 'תחנת החלל הבינלאומית',
     'דיפלומטיה של זכויות אדם', 'ניתוח מדיניות חוץ', 'אסטרטגיות דיפלומטיות', 'יוזמות דיפלומטיות',
     'שיתוף פעולה גלובלי', 'עניינים בינלאומיים', 'הסכמי שלום', 'תקשורת בין-תרבותית',
     'מנהיגות עולמית', 'מאמצים דיפלומטיים', 'ניתוח ענייני חוץ', 'דיאלוג דיפלומטי',
     'יחסי חוץ', 'קשרים דיפלומטיים', 'דיפלומטיה חוצת גבולות', 'בניית שלום', 'חיל דיפלומטי',
     'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'שיתוף פעולה בין-ממשלתי',
     'דיאלוג מדיני', 'דיפלומטיה כלכלית', 'יחסים דיפלומטיים', 'ביטחון בינלאומי',
     'מעורבות דיפלומטית', 'דיפלומטיה בינלאומית', 'דיפלומטיה רב-צדדית', 'שותפויות אסטרטגיות',
     'משימות דיפלומטיות', 'יוזמות דיפלומטיות', 'דיפלומטיה בין-תרבותית', 'משא ומתן גלובלי',
     'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי', 'יחסים בין-תרבותיים',
     'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי', 'משא ומתן לשלום', 'נוף גיאופוליטי',
     'ניתוח מדיניות חוץ', 'אמנות בינלאומיות', 'משא ומתן דיפלומטי', 'ענייני עולם',
     'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'דיפלומטיה כלכלית', 'חילופי תרבות',
     'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ', 'משימות דיפלומטיות', 'חסינות דיפלומטית',
     'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות', 'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי','משרד האומות המאוחדות לענייני החלל החיצון (UNOOSA)','UNOOSA',
     'קשרים דיפלומטיים', 'חוק בינלאומי', 'דיפלומטיה של זכויות אדם', 'סחר חוץ', 'פוליטיקה בינלאומית',
     'יחסים חוצי גבולות', 'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית',
     'ניתוח מדיניות חוץ', 'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים',
     'יחסים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי',
     'מאמצים דיפלומטיים', 'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית',
     'ביטחון בינלאומי', 'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית',
     'משא ומתן גלובלי', 'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי',
     'יחסים בין-תרבותיים', 'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי',
     'משא ומתן לשלום', 'נוף גיאופוליטי', 'ניתוח מדיניות חוץ', 'אמנות בינלאומיות',
     'משא ומתן דיפלומטי', 'ענייני עולם', 'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי',
     'דיפלומטיה כלכלית', 'חילופי תרבות', 'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ',
     'משימות דיפלומטיות', 'חסינות דיפלומטית', 'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות',
     'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי', 'קשרים דיפלומטיים', 'חוק בינלאומי',
     'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית', 'ניתוח מדיניות חוץ',
     'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים', 'יחסים דיפלומטיים',
     'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי', 'מאמצים דיפלומטיים',
      'יחסי חוץ', 'דיפלומטיה בינלאומית', 'ביטחון בינלאומי',
     'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי', 'יחסים בין-תרבותיים',
     'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי', 'משא ומתן לשלום', 'נוף גיאופוליטי',
     'ניתוח מדיניות חוץ', 'אמנות בינלאומיות', 'משא ומתן דיפלומטי', 'ענייני עולם',
     'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'דיפלומטיה כלכלית', 'חילופי תרבות',
     'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ', 'משימות דיפלומטיות', 'חסינות דיפלומטית',
     'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות', 'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי',
     'קשרים דיפלומטיים', 'חוק בינלאומי', 'פוליטיקה בינלאומית',
     'יחסים חוצי גבולות', 'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית',
     'ניתוח מדיניות חוץ', 'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים',
     'יחסים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי',
     'מאמצים דיפלומטיים', 'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית',
     'ביטחון בינלאומי', 'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית', 'תחנת חלל בינלאומית',
     'משא ומתן גלובלי', 'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי',
     'יחסים בין-תרבותיים', 'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי', 'סוכנות החלל',
     'משא ומתן לשלום', 'נוף גיאופוליטי', 'ניתוח מדיניות חוץ', 'אמנות בינלאומיות',
     'משא ומתן דיפלומטי', 'ענייני עולם', 'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי',
     'דיפלומטיה כלכלית', 'חילופי תרבות', 'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ',
     'משימות דיפלומטיות', 'חסינות דיפלומטית', 'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות',
     'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי', 'קשרים דיפלומטיים', 'חוק בינלאומי',
     'פוליטיקה בינלאומית',
     'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית', 'ניתוח מדיניות חוץ',
     'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים', 'יחסים דיפלומטיים',
     'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי', 'מאמצים דיפלומטיים',
     'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית', 'ביטחון בינלאומי',
     'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית', 'משא ומתן גלובלי',
     'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי', 'יחסים בין-תרבותיים',
     'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי', 'משא ומתן לשלום', 'נוף גיאופוליטי',
     'ניתוח מדיניות חוץ', 'אמנות בינלאומיות', 'משא ומתן דיפלומטי', 'ענייני עולם', 'יושב ראש',
     'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'דיפלומטיה כלכלית', 'חילופי תרבות',
     'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ', 'משימות דיפלומטיות', 'חסינות דיפלומטית',
     'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות', 'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי',
     'קשרים דיפלומטיים', 'חוק בינלאומי', 'פוליטיקה בינלאומית',
     'יחסים חוצי גבולות', 'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית',
     'ניתוח מדיניות חוץ', 'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים',
     'יחסים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי',
     'מאמצים דיפלומטיים', 'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית',
     'ביטחון בינלאומי', 'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית','אגנדה','#אגנדה',
     'משא ומתן גלובלי', 'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי', 'הוכרז',
     'יחסים בין-תרבותיים', 'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי',
     'משא ומתן לשלום', 'נוף גיאופוליטי', 'ניתוח מדיניות חוץ', 'אמנות בינלאומיות',
     'משא ומתן דיפלומטי', 'ענייני עולם', 'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי',
     'דיפלומטיה כלכלית', 'חילופי תרבות', 'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ','#Artemis','Artemis','Artemis Mission','Artemis Accords','Launch',
     'משימות דיפלומטיות', 'חסינות דיפלומטית', 'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות',
     'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי', 'קשרים דיפלומטיים', 'חוק בינלאומי',
     'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית', 'ניתוח מדיניות חוץ',
     'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים', 'יחסים דיפלומטיים',
     'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי', 'מאמצים דיפלומטיים',
     'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית', 'ביטחון בינלאומי',
     'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית', 'משא ומתן גלובלי',
     'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי', 'יחסים בין-תרבותיים',
     'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי', 'משא ומתן לשלום', 'נוף גיאופוליטי',
     'ניתוח מדיניות חוץ', 'אמנות בינלאומיות', 'משא ומתן דיפלומטי', 'ענייני עולם',
     'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'דיפלומטיה כלכלית', 'חילופי תרבות',
     'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ', 'משימות דיפלומטיות', 'חסינות דיפלומטית',
     'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות', 'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי',
     'קשרים דיפלומטיים', 'חוק בינלאומי', 'פוליטיקה בינלאומית',
     'יחסים חוצי גבולות', 'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית',
     'ניתוח מדיניות חוץ', 'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים',
     'יחסים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי',
     'מאמצים דיפלומטיים', 'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית',
     'ביטחון בינלאומי', 'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית',
     'משא ומתן גלובלי', 'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי',
     'יחסים בין-תרבותיים', 'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי',
     'משא ומתן לשלום', 'נוף גיאופוליטי', 'ניתוח מדיניות חוץ', 'אמנות בינלאומיות',
     'משא ומתן דיפלומטי', 'ענייני עולם', 'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי',
     'דיפלומטיה כלכלית', 'חילופי תרבות', 'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ',
     'משימות דיפלומטיות', 'חסינות דיפלומטית', 'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות',
     'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי', 'קשרים דיפלומטיים', 'חוק בינלאומי', 'משימת ירחי אפולו 11', 'אפולו 11',
     'יחסים חוצי גבולות',
     'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית', 'ניתוח מדיניות חוץ','ארטמיס'
     'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים', 'יחסים דיפלומטיים',
     'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי', 'מאמצים דיפלומטיים',
     'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית', 'ביטחון בינלאומי',
     'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית', 'משא ומתן גלובלי',
     'הסכמים בינלאומיים', 'קהילה דיפלומטית', 'פרוטוקול דיפלומטי', 'יחסים בין-תרבותיים', 'טיסת חלל אנושית',
     'שיח דיפלומטי', 'ממשל גלובלי', 'דיאלוג דיפלומטי', 'משא ומתן לשלום', 'נוף גיאופוליטי',
     'ניתוח מדיניות חוץ', 'אמנות בינלאומיות', 'משא ומתן דיפלומטי', 'ענייני עולם', 'תחנת החלל הבינלאומית',
     'דו קיום', 'מאמצים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'דיפלומטיה כלכלית', 'חילופי תרבות',
     'יציבות אזורית', 'קשרים דיפלומטיים', 'סיוע חוץ', 'משימות דיפלומטיות', 'חסינות דיפלומטית', 'קונגרס',
     'פסגות בינלאומיות', 'אסטרטגיות דיפלומטיות', 'שר חוץ', 'פרוטוקול', 'דיאלוג בינלאומי',
     'קשרים דיפלומטיים', 'חוק בינלאומי',  'עונת חגים',
     'יחסים חוצי גבולות', 'פרוטוקול דיפלומטי', 'מוסכמות בינלאומיות', 'קהילה דיפלומטית', 'אסטרונאוטים', 'תחנת החלל הבינלאומית',
     'ניתוח מדיניות חוץ', 'דיפלומטיה גלובלית', 'משא ומתן דיפלומטי', 'יחסים בין-ממשלתיים', 'טיסת חלל אנושית',
     'יחסים דיפלומטיים', 'שיתוף פעולה בינלאומי', 'תקשורת בינלאומית', 'דיאלוג פוליטי', 'צוות',
     'מאמצים דיפלומטיים', 'תקשורת בין-תרבותית', 'יחסי חוץ', 'דיפלומטיה בינלאומית',
     'ביטחון בינלאומי', 'מעורבות דיפלומטית', 'משימות דיפלומטיות', 'דיפלומטיה בין-תרבותית', 'משימות ארטמיס', 'גלובליות', 'תחרותיות בחלל'
     'משא ומתן גלובלי', 'הסכמים בינלאומיים', 'קהילה דיפלומטית',
     'משא ומתן לשלום', 'נוף גיאופוליטי', 'מדיניות חוץ', 'טלסקופ גיימס ווב', 'גיימס ווב', 'ארטמיס', 'משימה', 'הדגשים']

education_community_keywords =  ['חינוך', 'הסברה לקהילה','לוגו','עיצוב','נתראה שם!','שידור חי','פסטיבל','מטר מטאורים','חי כאן','חי','תחרות', 'למידה','מאמר חדש','צוות', 'השפעה חברתית','סגן מנהל','מרכז','טיסת חלל אנושית','וובינר','סטודנט','פרויקטים','פרויקט',' תואר ראשון','תואר שני',
     'בית ספר', 'תלמידים', 'מורים', 'כיתה', 'מערכת חינוך','טלסקופ גיימס ווב','גיימס ווב','ארטמיס','עודד','צעירים', 'הירשם','תייג ','copernicus eu','copernicus','workshop',
     'פיתוח קהילה', 'התנדבות', 'חונכות', 'מעורבות נוער','נוער','מדע','פורום','STEM','גילוי','פרופ','הצטרפו אלינו','סרטון ','אמן','מדיה חברתית','כיף','מטאור','מקלחת',
     'אקדמי', 'מלגה', 'אוריינות', 'העצמה', 'פיתוח מיומנויות', 'מחנכים', 'סדנאות', 'הצטרפו', 'מרכז גילוי', 'גילוי', 'מרכז', 'גלה עוד' ,'ESA','NASA','ESA','Congress',
     'תכנית חינוכית', 'הישגי תלמידים', 'משאבים חינוכיים', 'מחוז בית ספר','דברים שאתה צריך לדעת עליהם','הידעת','יופיטר','אמנות','חי עכשיו','# ארטמיס',
     'סביבת למידה', 'מדיניות חינוך', 'פיתוח תכניות לימודים', 'טכנולוגיה חינוכית', 'מסע דרך היקום שלנו','שבתאי','קרדיטים:','חי עכשיו','למידע נוסף','צפייה ישירה ',
     'חינוך STM', 'הכשרת מורים', 'חינוך כולל', 'חינוך מיוחד','אתגרים','סיור וירטואלי','עוף','קמפיין','כוכב','שנות אור מכדור הארץ',' שנות אור', 'אור', 'שנות אור'
     'בניין קהילה', 'מעורבות אזרחית', 'אחריות חברתית', 'פילנתרופיה','ניוזלטר','גלה','בתי ספר','ארגוני נוער','מרכזי מדע','סימפוזיון וירטואלי','וירטואלי', 'סִימפּוֹזִיוֹן',
     'ארגון ללא מטרות רווח', 'שירות קהילתי', 'קרן צדקה', 'צדק חברתי','הירשם עכשיו','הירשם','בקר במדריך שלנו','מוזיאונים','בית','מסיבת עיתונאים','עיתונות ','וְעִידָה',
     'מנהיגות בית ספרית', 'מעורבות הורים', 'קהילה לומדת', 'תוכנית צהריים', 'הידעת', 'הדגשות', 'שמעת אי פעם','אוריון','שמש','מרקורי',' ונוס','מארס','יופיטר','שבתאי','אורנוס','נפטון',
     'העצמת חינוך', 'יוזמה חינוכית', 'הסברה לחינוך', 'השפעה קהילתית','תמונת כדור הארץ','דגמי הדפסת תלת מימד','משחקי וידאו','ספר אלקטרוני',
     'העצמת נוער', 'רפורמה בחינוך', 'הסברה חינוכית', 'שוויון חינוכי','ליקוי ירח','תפוס','סיפור חדשותי','חדשות','עיתונות','נא להירשם',
     'הישגים חינוכיים', 'תמיכה בקהילה', 'חינוך לכולם', 'תוכנית חינוכית','גלקסיות','שביל החלב','עונת חגים','סדנא מקוונת','סגל','חוקרים','חוקרים ','אקדמיה',
     'שיתוף פעולה קהילתי', 'שיפור בית ספר', 'חדשנות חינוכית', 'בניין קהילה','משימה','שנות אור','מסיבת עיתונאים',
     'פיתוח נוער', 'מודעות לחינוך', 'חינוך קהילתי', 'הזדמנויות חינוכיות','צילום: נאס"א','שבוע החלל','תחנת החלל הבינלאומית','בינלאומי', 'חלל', 'תחנה',
     'חינוך לפיתוח בר קיימא', 'יוזמת חינוך', 'תוכנית לפיתוח קהילה','משימות ארטמיס','משימת אפולו 11 לירח','אפולו 11',
     'העצמה חינוכית', 'מעורבות קהילתית', 'שותפות בית ספרית', 'הסברה חינוכית','ליקוי ירח','ליקוי חמה','נאס"א',
     'העשרה בחינוך', 'תמיכה חינוכית', 'מעורבות קהילה', 'יוזמת חינוך','STEM','Webb','בחלל','חג המולד','השקה','שבוע החלל','אולימפיאדת החלל','ירח','מאדים','ארטמיס'
     'חינוך מבוסס קהילה', 'גישה לחינוך', 'הכללת חינוך', 'יוזמה לפיתוח קהילה', 'ערפילית', 'ראיון','גשושית'
     'מנהיגות נוער', 'מנהיגות חינוכית', 'העשרה בקהילה', 'חינוך לשינוי חברתי', 'אתגר', 'טיסת חלל אנושית',
     'קהילת בית ספר', 'פיתוח חינוכי', 'תכנית לחינוך קהילתי', 'תכנית לחינוך נוער',' חקר החלל', 'חפצי חלל', 'יום האקדמיה',
     'השפעה חינוכית', 'מודעות קהילתית', 'טרנספורמציה בחינוך', 'למידה בקהילה','הישאר מעודכן','אסטרונאוט','טריילר לסרט','מאמר',
     'שיתוף פעולה חינוכי', 'קהילה מכילה', 'התקדמות בחינוך', 'שינוי קהילתי', 'חוויה', 'חגים',
     'הישג חינוכי', 'העצמה קהילתית', 'מעורבות בחינוך', 'הסברה לצעירים', 'מסע דרך היקום שלנו',
     'קידום חינוכי', 'יוזמה קהילתית', 'שוויון בחינוך', 'שותפות קהילתית','חי עכשיו','משפר','פאנל',
     'שוויון חינוכי', 'תוכנית תמיכה בקהילה', 'יוזמת חינוך', 'העשרה בקהילה', 'סיפורים', 'מטרי מטאורים',
     'התקדמות חינוכית', 'צמיחה קהילתית', 'שותפות בחינוך', 'יוזמה לחינוך קהילתי','הגעה אל','צפה בשידור חי','מאדים','ירח','אפולו 11','למידע נוסף על' ,
     'שינוי חינוכי', 'תוכנית מעורבות קהילתית', 'חדשנות בחינוך', 'יוזמה לפיתוח קהילה', 'שנה טובה',
     'תכנית לפיתוח חינוכי', 'יוזמה לבניית קהילה', 'תכנית הסברה לחינוך', 'תכנית לפיתוח נוער',
     'תוכנית לשינוי חינוכי', 'יוזמה לתמיכה בקהילה',
     'תוכנית להעצמת חינוך', 'השפעה על פיתוח קהילה', 'יוזמה חינוכית', 'תוכנית למודעות קהילתית', 'עכשיו אתה יכול לחקור',
     'תוכנית תמיכה בחינוך', 'יוזמת מעורבות קהילתית', 'תוכנית השפעה חינוכית', 'יוזמה לשינוי קהילה',
     'יוזמת חינוך', 'שיתוף פעולה לפיתוח קהילה', 'שיתוף פעולה חינוכי', 'יוזמת למידה קהילתית',
     'תוכנית שותפות בחינוך', 'שיתוף פעולה תמיכה בקהילה', 'שיתוף פעולה לשינוי חינוכי', 'יוזמה להעצמת קהילה',
     'תוכנית שיתוף פעולה בחינוך', 'מעורבות בפיתוח קהילה', 'שיתוף פעולה עם השפעה חינוכית', 'יוזמה לשיתוף פעולה בקהילה', 'מרחב וקיימות',
     'תוכנית לשינוי חינוך', 'יוזמה לצמיחה קהילתית', 'שיתוף פעולה התקדמות חינוכית', 'תוכנית שותפות קהילתית', 'שביל החלב', 'אסטרונאוטים',
     'יוזמה להעצמת חינוך', 'שיתוף פעולה להעשרה בקהילה', 'תוכנית שוויון חינוכי', 'טרנספורמציה של תמיכה בקהילה', 'מערכת שמש',
     'יוזמת חינוך', 'חדשנות לפיתוח קהילה', 'חדשנות חינוכית', 'תוכנית למידה קהילתית',' סיור', 'סיור', 'אירועי אקלים',
     'יוזמת שותפות בחינוך', 'חדשנות תומכת בקהילה', 'מטר מטאורים', 'חדשנות לשינוי חינוכי', 'תוכנית להעצמת קהילה', 'קריירה',
     'תוכנית חדשנות בחינוך', 'יוזמה להשפעה לפיתוח קהילה', 'יוזמת הסברה חינוכית', 'תוכנית מודעות לקהילה', 'שבוע החלל',
     'יוזמת תמיכה בחינוך', 'חדשנות מעורבות בקהילה', 'תוכנית השפעה חינוכית', 'יוזמה לשינוי קהילה', 'קונגרס אסטרונאוטי בינלאומי',
     'יוזמה חינוכית', 'תוכנית שיתוף פעולה לפיתוח קהילה', 'מפגש', 'הירשם', 'יוזמת שיתוף פעולה חינוכית', 'יוזמת למידה קהילתית',
     'תוכנית שותפות בחינוך', 'יוזמה לשיתוף פעולה תמיכה בקהילה', 'תוכנית לשיתוף פעולה לשינוי חינוכי', 'יוזמה להעצמת קהילה',
     'תוכנית יוזמת שיתוף פעולה בחינוך', 'יוזמת מעורבות לפיתוח קהילה', 'תוכנית שיתוף פעולה להשפעה חינוכית', 'תוכנית יוזמה קהילתית',
     'יוזמת תוכנית לשינוי חינוך', 'תוכנית יוזמה לצמיחה קהילתית', 'יוזמה לשיתוף פעולה התקדמות חינוכית', 'יוזמת תוכנית שותפות קהילתית',
     'תוכנית יוזמה להעצמת חינוך', 'הידעת', 'השראה', 'כוח עבודה עתידי בחלל', 'יוזמת שיתוף פעולה להעשרה בקהילה', 'יוזמת תוכנית שוויון חינוכית', 'יוזמה לשינוי תמיכה בקהילה', 'יוזמת חינוך']
space_industry_keywords = [
'מגזר החלל','תעשיית החלל','עסקים','מנהיגים','מחשוב קצה החלל','מחשוב קצה','תעשייה','חברות','ייצור',
     'רקטה', 'קוסמוס', 'מסלול', 'חללית', 'חוץ כדור הארץ', 'טלסקופ גיימס ווב', 'גיימס ווב', 'STEM', 'תעשיות חלל',
     'שמימי','כוכב הלכת','קוסמונאוט','סוכנות החלל','סדנאות','הזדמנויות חדשות','הזדמנויות השקעה','השקעה','השקעות','הזדמנויות','לאומיות',
     'בין-כוכבי', 'טכנולוגיית חלל', 'אסטרונאוט', 'תחנת חלל','מגזר החלל','מגזר','השקת אפליקציות','השקה','יישומים',
     'גלקסיה', 'מערכת שמש', 'קוסמית', 'חקר', 'כוכבים', 'מגזר', 'עדכוני תעשייה', 'פעילויות רגולטוריות', 'תעשיית החלל', 'גיוס', 'השקה',
     'בין כוכבי לכת', 'מחקר חלל', 'קרניים קוסמיות', 'אסטרונומיות', 'תצפית', 'כלכלה', 'SpaceX', 'נכסים תעשייתיים', 'תעשייתיים',
     'אסטרופיזיקה', 'מסעות בחלל', 'כבידה', 'מדעי החלל', 'אסטרוביולוגיה', 'אתגרים',
     'אבק קוסמי', 'אבולוציה של כוכבים', 'מסובב', 'שיגור חלל', 'אסטרוצלם',
     'מעבורת חלל', 'חדשנות בחלל', 'חיים מחוץ לכדור הארץ', 'פלנטריום', 'הליכת חלל',
     'חללית', 'תופעות חלל', 'מזג אוויר בחלל', 'סוכנות חלל', 'קרינה קוסמית',
     'תצפית בחלל', 'שיגור רקטה', 'חקר חלל', 'טיסת חלל אנושית',
     'טכנולוגיית חלל', 'שיגור לווין', 'טלסקופ חלל', 'מדע טילים', 'קולוניזציה בחלל', 'יופיטר', 'אוראורות',
     'מדיניות חלל', 'חדשות תעשיית החלל', 'ארגון מחקר חלל', 'מרוץ לחלל', 'קשור לחלל',
     'מכניקת מסלול', 'תקשורת חלל', 'מחקר מדעי החלל', 'פיתוח טכנולוגיית חלל', 'עדכוני משימת חלל',
     'הנעת רקטה', 'חדשנות במסע בחלל', 'גופים שמימיים', 'חקירת אסטרואידים',
     'תופעות קוסמיות', 'תגליות חלל', 'שיתוף פעולה של סוכנויות חלל', 'חקירה פלנטרית', 'מחקר תחנות חלל', 'טכנולוגיית לייזר',
     'חקירה גלקטית', 'תגליות אסטרונומיות', 'פיתוח חלליות', 'תגליות חלל', 'רובר', 'סטארלינק',
     'התקדמות תעשיית החלל', 'שיתוף פעולה בינלאומי בחלל', 'אבני דרך של חקר החלל', 'טכנולוגיית חקר החלל', 'משימות חקר החלל',
     'טכנולוגיית רקטות', 'פריצות דרך בחקר החלל', 'ממצאי מחקר החלל', 'הצלחת משימות חלל', 'טכנולוגיית לווין',
     'יוזמות חקר החלל', 'תגליות מדעי החלל', 'עדכוני חקר החלל', 'הישגי האסטרונאוטים', 'פיתוחי תעשיית החלל',
     'משימות מסלול', 'חקירה בין-פלנטרית', 'הישגי סוכנות החלל', 'פסולת חלל',
     'שיתופי פעולה בחקר החלל', 'חידושים בטכנולוגיית חלל', 'תקשורת לוויינית', 'כנסים של תעשיית החלל', 'מחקר מדע פלנטרי',
     'מגמות תעשיית החלל', 'היסטוריה של חקר החלל', 'חקר קוסמי', 'בטיחות במסעות בחלל', 'אתגרי תעשיית החלל',
     'טכנולוגיות שיגור רקטות', 'התקדמות במדעי החלל', 'מחקר מכניקת מסלול', 'תיעודי חקר החלל', 'השפעה על תעשיית החלל',
     'הסכמי חלל בינלאומיים', 'משימות חקר החלל', 'שותפויות בתעשיית החלל', 'הצלחות שיגור רקטות', 'יישומי טכנולוגיית חלל',
     'תצפית בגופים שמימיים', 'פריצות דרך אסטרונומיות', 'טכנולוגיות חלליות', 'סרטי תעודה של חקר החלל', 'התקדמות שיגור רקטות',
     'חידושי מכניקת מסלול', 'כנסים של תעשיית החלל', 'יוזמות מחקר חלל', 'הישגי חקר החלל', 'יעדי חקר החלל',
     'טכנולוגיות תקשורת לווייניות', 'שיתופי פעולה בתעשיית החלל', 'חידושים להנעת רקטות', 'כנסים של טכנולוגיית חלל', 'היסטוריה של חקר החלל',
     'סרטי תעודה של חקר קוסמי', 'אמצעי בטיחות בנסיעות בחלל', 'אתגרים ופתרונות של תעשיית החלל', 'השפעה של תעשיית החלל על החברה',
     'אמצעי בטיחות לשיגור רקטות', 'מחקר טכנולוגיית חלל', 'טכנולוגיות תצפית בגופים שמימיים', 'קריירה', 'עבודות', 'לגדול',
     'תיעוד תגליות אסטרונומיות', 'פיתוח טכנולוגיות חלליות', 'השפעה על סרטי תעודה של חקר החלל', 'התקדמות טכנולוגיות שיגור רקטות', 'תוצאות כנסים בתעשיית החלל',
     'תוצאות של יוזמות מחקר חלל', 'השפעה על הישגי חקר החלל', 'תוצאות יעדי חקר החלל', 'השפעת טכנולוגיות תקשורת לוויינית', 'תוצאות שיתופי פעולה בתעשיית החלל',
     'תוצאות חידושי הנעת רקטות', 'תוצאות כנסים בטכנולוגיית חלל', 'תיעוד היסטוריית חקר החלל', 'השפעה של סרטי תעודה של חקר קוסמי', 'תוצאות אמצעי בטיחות במסעות בחלל',
     'אתגרים ותוצאות פתרונות של תעשיית החלל', 'השפעה של תעשיית החלל על תוצאות החברה', 'תוצאות שותפויות בחקר החלל','SpaceX',
     'טכנולוגיות תקשורת לווייניות משפיעות על החברה', 'השפעת שיתופי פעולה בתעשיית החלל', 'השפעת חידושי הנעת רקטות', 'השפעה של כנסים בטכנולוגיית חלל',
     "השפעה של סרטי תעודה של חקר קוסמי על החברה", "השפעה של אמצעי בטיחות בנסיעות בחלל", "השפעה של אתגרי תעשיית החלל ופתרונות תוצאות", "מגמות חקר החלל משפיעות על החברה", 'טכנולוגיות תקשורת לווייניות משפיעות על החברה', 'השפעת שיתופי פעולה בתעשיית החלל'', ',
     "השפעה של סרטי תעודה של חקר קוסמי על החברה", "השפעה של אמצעי בטיחות בנסיעות בחלל", "השפעה של אתגרי תעשיית החלל ופתרונות תוצאות", "מגמות חקר החלל משפיעות על החברה",
     'השפעה של תעשיית החלל על השפעת תוצאות החברה', 'השפעת אמצעי בטיחות שיגור רקטות', 'השפעת תוצאות מחקר טכנולוגיית החלל',
     "טכנולוגיות תצפית של גופים שמימיים משפיעות על החברה", "השפעה של תיעוד תגליות אסטרונומיות על החברה", "השפעה של טכנולוגיות חלליות על פיתוח תוצאות", "השפעה של סרטי תעודה של חקר החלל על תוצאות החברה",
     'טכנולוגיות שיגור רקטות משפיעות על החברה', 'תוצאות כנסים של תעשיית החלל השפעות על החברה', 'תוצאות מחקר החלל השפעות על החברה', 'הישגי חקר החלל משפיעים על תוצאות החברה', 'חוק החלל', 'חוק החלל הבינלאומי' , 'אמנת החלל החיצון']

research_technology_keywords = [ 
    'ארגון מחקר', 'טכנולוגיה', 'לוויין', 'טלסקופ', 'אסטרונומיה', 'חדשנות', 'פאנל', 'מערכת סולארית', 'סגן מנהל', 'צוות', 'מטר מטאורים', 'מטאור' ,'טיסת חלל','התקדמות מדעית','מופ','ערפילית','בינה מלאכותית','למידת מכונה','עיבוד קצה','תיאוריות',
     'מחקר מדעי', 'מעבדה', 'ניסוי', 'גילוי', 'טיסת חלל אנושית', 'המצאה', 'מחשוב קצה החלל', 'מחשוב קצה', 'ארטמיס', 'ד"ר', 'פסולת חלל' ,
     'חוקר', 'מדען', 'פריצת דרך', 'ניתוח נתונים', 'קדמה טכנולוגית', 'אתגרים גלובליים', 'שינויי אקלים', 'אסונות טבע', 'נטו אפס', 'SpaceX',
     'חדשני', 'אב טיפוס', 'ביוטכנולוגיה', 'ננוטכנולוגיה', 'הנדסה', 'טלסקופ גיימס ווב', 'גיימס ווב', 'ד"ר', 'מדען ראשי', 'מדען',
     'מחקר', 'מחקר אקדמי', 'מתודולוגיית מחקר', 'פרויקט מחקר', 'תחרות', 'שיגור רקטות', 'קהילה מדעית', 'משימה', 'STEM', 'אורורה', 'שנות אור מכדור הארץ',
     'ממצאי מחקר', 'מאמר מחקר', 'מכון מחקר', 'מענק מחקר', 'שיתוף פעולה מחקרי', 'מערכת שמש', 'מדע', 'אוראורות','גשושית','סייבר','אסטרונאוט','אסטרונאוטית',
     'מחקר ופיתוח', 'טכנולוגיה חדשנית', 'טכנולוגיה מתפתחת', 'מגמות טכנולוגיות', 'העברת טכנולוגיה', 'מאדים', 'מערכות חלל','ארטמיס',
     'אימוץ טכנולוגיה', 'שילוב טכנולוגי', 'חדשנות טכנולוגית', 'חדשנות מחקרית', 'גילוי מדעי', 'אסונות טבע',
     'קהילה מדעית', 'ספרות מדעית', 'כתב עת מדעי', 'ביקורת עמיתים', 'כנס מדעי', 'שריפות', 'הצפה', 'שיגור',
     'מחקר ניסיוני', 'מחקר יישומי', 'מחקר יסודי', 'פריצת דרך מדעית', 'פרסום מחקר', 'ליקוי ירח',
     'אתיקה מחקרית', 'מימון מחקר', 'תוצאות מחקר', 'השפעה מחקרית', 'תוצאות מחקר', 'איכות מחקר', 'משימות ארטמיס', 'מחקר ביו-רפואי', 'ביו-רפואי',
     'מגזר טכנולוגי', 'פתרונות טכנולוגיים', 'טכנולוגיה מתקדמת', 'טכנולוגיה מתקדמת', 'פיתוח טכנולוגי', 'שנות אור',
     'הערכה טכנולוגית', 'מערכת אקולוגית של חדשנות', 'תשתית מחקר', 'מצוינות מחקר', 'התקדמות טכנולוגית', 'ליקוי חמה', 'שבתאי',
     'שותפות מחקר', 'שיתוף פעולה במחקר', 'רשת מחקר', 'סטנדרטים טכנולוגיים', 'יוזמת מחקר', 'הצד הרחוק של הירח', 
     'התכנסות טכנולוגית', 'מרכז מחקר', 'מונע טכנולוגיה', 'מתקני מחקר', 'ניהול טכנולוגיה', 'כדור הארץ', 'רובר', 'חמצן', 'יושב ראש',
     'תוכנית מחקר', 'השקעה בטכנולוגיה', 'אסטרטגיית חדשנות', 'מערכת אקולוגית של מחקר', 'שוק טכנולוגיה', 'אסטרונומים', 'אסטרואיד', 'קונגרס',
     'מיקוד מחקר', 'נוף טכנולוגי', 'מרכז מחקר', 'מרכז טכנולוגי', 'אתגרי מחקר', 'אתגרים טכנולוגיים', 'שביל החלב', 'סטרטוספירה',
     'פריצות דרך מחקר', 'השפעה טכנולוגית', 'מחקר וחדשנות', 'פריסת טכנולוגיה', 'מחקר ופיתוח', 'אטמוספירה נמוכה יותר', 'אטמוספירה',
     'פתרונות טכנולוגיים', 'השפעה מחקרית', 'מגמות טכנולוגיות', 'שילוב מחקר', 'אימוץ טכנולוגיה', 'חיזוי מזג אוויר', 'אירועי אקלים',
     'גבול מחקר', 'גבול טכנולוגי', 'נוף מחקר', 'נוף טכנולוגי', 'אגנדה מחקרית', 'שמיים', 'ליקוי ירח','חור שחור','מטאורים'
     'אגנדה טכנולוגית', 'מתודולוגיות מחקר', 'טרנספורמציה טכנולוגית', 'מנהיגות מחקר', 'מנהיגות טכנולוגית', 'כוכב', 'גלקסיות', 'ונוס',
     'יכולות מחקר', 'יכולות טכנולוגיות', 'שיתוף פעולה במחקר', 'שיתוף פעולה טכנולוגי', 'קידום מחקר', 'רובר', 'סדנה מקוונת', 'פקולטה', 'מחקר', 'חוקרים', 'אקדמיה',
     'התקדמות טכנולוגית', 'תוצאות מחקר', 'תוצאות טכנולוגיות', 'מצוינות מחקרית', 'מצוינות טכנולוגית', 'מטרי מטאורים', 'יום האקדמיה',
     'אסטרטגיית מחקר', 'אסטרטגיה טכנולוגית', 'מחקר וטכנולוגיה', 'טכנולוגיה וחדשנות', 'מחקר ופיתוח', 'אגמים', 'נהרות', 'זרימה', 'סביבה', 'שינויי אקלים',' דיג','אוקיינוסים',
     'טכנולוגיה וחברה', 'מחקר ותעשייה', 'טכנולוגיה וקידמה', 'מחקר וחדשנות', 'ירח', 'אנטנת חלל עמוק', 'חלל עמוק',
     'טכנולוגיה וקידמה', 'מגמות מחקר וטכנולוגיה', 'טכנולוגיה ועתיד', 'מגמות מחקר ופיתוח', 'אסטרוצלם', 'הידרולוגיה', 'אוקיאנוגרפיה', 'ווב',
     'מגמות טכנולוגיה וחדשנות', 'השפעה מחקרית וטכנולוגית', 'השפעה טכנולוגית וחברתית', 'השפעת מחקר ופיתוח', 'שריפות יער',
     'טכנולוגיה ועסקים', 'פתרונות מחקר וטכנולוגיה', 'אתגרים טכנולוגיים וגלובליים', 'שילוב מחקר וטכנולוגיה', 'CubeSats',
     'טכנולוגיה וצמיחה כלכלית', 'מחקר והתכנסות טכנולוגית', 'טכנולוגיה וקיימות', 'שיתוף פעולה במחקר וטכנולוגיה', 'רוזטה', 'פסולת חלל',
     'התקדמות הטכנולוגיה והמחקר', 'חדשנות וטכנולוגיה', 'התקדמות מחקר וטכנולוגיה', 'מצוינות טכנולוגיה ומחקר',
     'שותפות מחקר וטכנולוגיה','מתקני מחקר ', 'השקעה במחקר וטכנולוגיה', 'יכולות טכנולוגיה ומחקר', 'תחנת מחקר',
     'פריסה של מחקר וטכנולוגיה', 'אגנדה של טכנולוגיה ומחקר', 'מנהיגות מחקר וטכנולוגיה', 'טרנספורמציה של טכנולוגיה ומחקר',
     'נוף מחקר וטכנולוגיה', 'אתגרי טכנולוגיה ומחקר', 'תוצאות מחקר וטכנולוגיה', 'טכנולוגיה ומחקר אסטרטגיית', 'COSPAR',' Copernicus EU',
     'שיתוף פעולה במחקר וטכנולוגיה', 'קידום טכנולוגיה ומחקר', 'תוצאות מחקר וטכנולוגיה', 'מצוינות טכנולוגיה ומחקר', 'נאס"א', 'עומס מטען', 'דחף ואקום',
     'אסטרטגיית מחקר וטכנולוגיה', 'יכולות טכנולוגיה ומחקר', 'שמש', 'פתרונות מחקר וטכנולוגיה', 'השפעה של טכנולוגיה ומחקר',
     'שילוב מחקר וטכנולוגיה', 'חדשנות טכנולוגיה ומחקר', 'חזית מחקר וטכנולוגיה', 'נוף טכנולוגיה ומחקר', 'קרא עוד',
     'טרנספורמציה של מחקר וטכנולוגיה', 'מתודולוגיות טכנולוגיה ומחקר', 'התכנסות מחקר וטכנולוגיה', 'שותפות טכנולוגיה ומחקר', 'צף מראה', 'גלי חלל',
     'פריסה של מחקר וטכנולוגיה', 'תשתית טכנולוגיה ומחקר', 'שיתוף פעולה במחקר וטכנולוגיה', 'רשת טכנולוגיה ומחקר',
     'מרכז מחקר וטכנולוגיה', 'תוכנית טכנולוגיה ומחקר', 'מתקני מחקר וטכנולוגיה', 'מיקוד טכנולוגיה ומחקר', 'טכנולוגיית לייזר', 'מחקר במדינות מתפתחות',
     'מנהיגות מחקר וטכנולוגיה', 'אתגרי טכנולוגיה ומחקר', 'השפעה מחקרית וטכנולוגית', 'לגלות',
     'מרכז מחקר וטכנולוגיה', 'שוק טכנולוגיה ומחקר', 'פריסה של מחקר וטכנולוגיה', 'אתגרי טכנולוגיה ומחקר', 'פעילויות ניהול תעבורה בחלל',
     'התקדמות מחקר וטכנולוגיה', 'תוצאות טכנולוגיה ומחקר', 'פתרונות מחקר וטכנולוגיה', 'טכנולוגיה ומחקר אקולוגי', 'אוריון', 'שמש', 'מרקורי', 'ונוס', 'מאדים', 'יופיטר ','שבתאי','אורנוס','נפטון',
     'יכולות מחקר וטכנולוגיה', 'התכנסות טכנולוגיה ומחקר', 'נוף מחקר וטכנולוגיה', 'מצוינות טכנולוגיה ומחקר', 'קיימות', 'טכנולוגיות',
     'אסטרטגיית מחקר וטכנולוגיה', 'שותפות טכנולוגיה ומחקר', 'מחקר וחדשנות טכנולוגית', 'טרנספורמציה של טכנולוגיה ומחקר', 'סביבת חלל',
     'מנהיגות מחקר וטכנולוגיה', 'התקדמות טכנולוגיה ומחקר', 'השקעה במחקר וטכנולוגיה', 'שילוב טכנולוגיה ומחקר', 'קופרניקוס EMS',
     'פריסה של מחקר וטכנולוגיה', 'תוצאות מחקר וטכנולוגיה', 'אסטרטגיית טכנולוגיה ומחקר', 'קופרניקוס האיחוד האירופי','קופרניקוס האיחוד האירופי','קופרניקוס'
     'שיתוף פעולה בין מחקר וטכנולוגיה', 'נוף טכנולוגי ומחקר', 'אתגרי מחקר וטכנולוגיה', 'תוצאות טכנולוגיה ומחקר', '#ארטמיס','מרכז החלל קנדי',
     'פתרונות מחקר וטכנולוגיה', 'מצוינות טכנולוגיה ומחקר', 'השפעה מחקרית וטכנולוגית', 'שילוב טכנולוגיה ומחקר', 'תחנת החלל הבינלאומית',
     'התכנסות מחקר וטכנולוגיה', 'פריסה של טכנולוגיה ומחקר', 'שותפות מחקר וטכנולוגיה', 'מתקני טכנולוגיה ומחקר', 'ירח למאדים', 'ירח', 'מאדים',
     'טרנספורמציה של מחקר וטכנולוגיה', 'מיקוד טכנולוגיה ומחקר', 'אסטרונאוט', 'מנהיגות מחקר וטכנולוגיה', 'אגנדה של טכנולוגיה ומחקר', 'גלה עוד',
     'מרכז מחקר וטכנולוגיה', 'תוכנית טכנולוגיה ומחקר', 'תשתית מחקר וטכנולוגיה', 'קופרניקוס', 'רשת טכנולוגיה ומחקר', 'מאדים', 'מחזורי מים', 'תצפית כדור הארץ',
     'מרכז מחקר וטכנולוגיה', 'אקוסיסטם טכנולוגי ומחקר', 'השקעה במחקר וטכנולוגיה', 'יכולות טכנולוגיה ומחקר','ד"ר','#NASA','#ESA','#JAXA','# ISRO','#CSA','#UKSA','#UAESA','#LSA','#ISA','#DLR','#CNES',
     'פריסה של מחקר וטכנולוגיה', 'התכנסות טכנולוגיה ומחקר', 'נוף מחקר וטכנולוגיה', 'עננים', 'מומחיות טכנית', 'מצוינות טכנולוגיה ומחקר', 'מדען פלנטרי',
     'מרכז לתצפית כדור הארץ', 'מומחה', 'תצפית כדור הארץ', 'מטאורולוגיה', 'מזג אוויר', 'ליקוי ירח', 'מחקר תרופות בחלל', 'מחקר תרופות', 'לחות קרקע', 'לוויינים', 'סוג צמחייה','שימוש קרקע','פרופ','מערכת שמש']

# Create a dictionary mapping each category to its corresponding keywords
keywords_dict = {
    'International Relations': international_relations_keywords,
    'Education and Community': education_community_keywords,
    'Space Industry': space_industry_keywords,
    'Research and Technology': research_technology_keywords
}

# Create columns for each field
for field in keywords_dict.keys():
    data[f"{field}_Related"] = 0

# Function to classify posts based on the presence of keywords
def classify_posts(row, keywords_dict):
    # Check if the value in the 'Message' column is a string
    if isinstance(row['Message'], str):
        post = row['Message'].lower()  # Convert post text to lowercase
        word_count = count_words(post)

        # Set 1 for each field where there are related keywords
        for field in keywords_dict.keys():
            row[f"{field}_Related"] = int(any(keyword in word_count for keyword in keywords_dict[field]))
    return row

# Apply the updated classification function to categorize posts
data = data.apply(classify_posts, axis=1, keywords_dict=keywords_dict)

# Save the updated DataFrame to a new CSV file
output_file_path = 'C:\\Users\\shake\\Desktop\\MSC- Data Science\\Thesis\\Tables\\Agancies Data-CrowdTangle\\ISA2.csv'
data.to_csv(output_file_path, index=False,encoding='utf-8')

# Display the updated classification in the DataFrame
print(data[['Message', 'International Relations_Related', 'Education and Community_Related', 'Space Industry_Related', 'Research and Technology_Related']])