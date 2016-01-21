##Crashing Android Messaging App{:.blog-post-title}

February 14, 2013
{:.blog-post-meta}


Recently, I decided to downgrade my phone from CyanogenMod 10.1 (Jelly Bean) to CyanogenMod 9.1 (ICS). I wanted to keep a few things, like Camera pictures and SMS. Android stores MMS and SMS messages in a SQLite database located in ./data/data/com.android.providers.telephony/databases/mmssms.db. I simply copied the mmssms.db file off my device before installing CM9.1. A problem arose when the Messaging app started crashing after replacing the mmssms.db in the freshly installed OS. Running logcat and opening Messaging app generated this error:


	/DatabaseUtils( 2527): android.database.sqlite.SQLiteException: Can't upgrade read-only database from version 57 to 55: /data/data/com.android.providers.telephony/databases/mmssms.db
	E/DatabaseUtils( 2527):     at android.database.sqlite.SQLiteOpenHelper.getReadableDatabase(SQLiteOpenHelper.java:244)
	E/DatabaseUtils( 2527):     at com.android.providers.telephony.MmsSmsProvider.query(MmsSmsProvider.java:286)
	E/DatabaseUtils( 2527):     at android.content.ContentProvider$Transport.query(ContentProvider.java:178)
	E/DatabaseUtils( 2527):     at android.content.ContentProviderNative.onTransact(ContentProviderNative.java:112)
	E/DatabaseUtils( 2527):     at android.os.Binder.execTransact(Binder.java:338)
	E/DatabaseUtils( 2527):     at dalvik.system.NativeStart.run(Native Method)

After some investigation I found the answer on StackOverflow: <http://stackoverflow.com/questions/8030779/change-sqlite-database-version-number>

You can manually set the user_version of the SQLite database by entering PRAGMA user_version = 55; After I made this change, the Messaging app opened normally and there were no errors when watching logcat. Simple fix.

Some additional information about  SQLite versions: <https://www.sqlite.org/pragma.html#pragma_schema_version>