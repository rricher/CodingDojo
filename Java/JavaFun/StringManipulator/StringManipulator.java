public class StringManipulator {
    public String trimAndConcat(String str1, String str2) {
        str1 = str1.trim();
        str2 = str2.trim();
        return str1 + str2;
    }

    public Integer getIndexOrNull(String str, char chr) {
        Integer i;
        i = str.indexOf(chr);
        if (i == -1) {
            return null;
        } else {
            return i;
        }
    }

    public Integer getIndexOrNull(String str, String subStr) {
        Integer i;
        i = str.indexOf(subStr);
        if (i == -1) {
            return null;
        } else {
            return i;
        }
    }

    public String concatSubstring(String str1, int start, int end, String str2) {
        str1 = str1.substring(start, end);
        return str1 + str2;
    }
}