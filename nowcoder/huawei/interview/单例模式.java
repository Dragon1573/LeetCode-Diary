package nowcoder.huawei.interview;

/** 饥饿模式 */
class Singleton01 {
    private static Singleton01 instance = new Singleton01();

    private Singleton01() {
    }

    public static Singleton01 getInstance() {
        return instance;
    }
}

/** 惰性加载（线程不安全） */
class Singleton02 {
    private static Singleton02 instance;

    private Singleton02() {
    }

    public static Singleton02 getInstance() {
        if (instance == null) {
            instance = new Singleton02();
        }
        return instance;
    }
}

/** 惰性加载（线程不安全） */
class Singleton03 {
    private static Singleton03 instance;

    private Singleton03() {
    }

    public static synchronized Singleton03 getInstance() {
        if (instance == null) {
            instance = new Singleton03();
        }
        return instance;
    }
}

/** 双重检查 DCL （线程安全） */
class Singleton04 {
    private volatile static Singleton04 instance;

    private Singleton04() {
    }

    public static Singleton04 getInstance() {
        if (instance == null) {
            synchronized (Singleton04.class) {
                if (instance != null) {
                    instance = new Singleton04();
                }
            }
        }
        return instance;
    }
}
