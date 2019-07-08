class StringsDemo{
	public static void main(String []args){
		String s=" name SURNAME ";
		System.out.println(s.toUpperCase());
		System.out.println(s.toLowerCase());
		System.out.println(s.length());
		System.out.println(s.trim());
		System.out.println(s.replace("na","ta"));
		System.out.println(s.startsWith("SU"));
		System.out.println(s.endsWith("ME "));
		System.out.println(s.charAt(2));
		System.out.println(s.valueOf(s));
	}
}