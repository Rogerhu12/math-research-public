# 曲率缺陷 guard：只续未完成四项，复用已付14项

日期：2026-11-15。前次真实失败见 [首开发记录](observed-curvature-defect-guard-first-development-failure-20261115.md)。这里提交最小修复与严格续入口；**尚未宣告第四组通过或科学运行完成**。

## 修改与复用边界

只改两份新文件，生产core/recovery/transfer三源和旧135份Python逐字保留，合计138份不变；6份workflow也不变。

- 开发文件 32867B，SHA256 5e5e2090a66af2bfcc07bc8a61ca41b1a4ac1d55afcd96e12e8ca2a11475d75f。第四组人工base_init删除唯一错误的fixed_zeta setter赋值；该只读property从cfg读取。根文本diff确认：新resume函数之前只有这一行删除，前三已付函数及所有共享helper逐字相同。
- audit 37203B，SHA256 86f3d51eb5159165120dd846c6f800d4ed73fcde0cc31a7c331103049550a7ae。只增加原失败日志的严格收据读取及主入口调用；不改变生产算法、原实际门、cfg/g/b0/reference、预算或科学driver。

新developer_check必须收到paid_development参数。它核原policy/schema、四组顺序、前三5/5/4全部true、第四精确只读property错误、原core/outer/dev SHA及原科学/旧suite调用0；复制前三group原判定，不执行其函数。它唯一运行第四组375-entry及样本绑定，输出new1组/4项与reused3组/14项，合并的18项总判定不冒为本次全执行。没有原回执直接拒绝，防止误重跑已付14项。

## 原失败日志的准确来源核对

audit新增read_paid_first_fourteen_development明确要求原run43766593534/job132972995287/sourcea48f3398fc587cc1370a26a56978e719629b878c是completed/**failure**。它不调用原success-only科学completed_log，也不把失败run当已完成的科学checkpoint。

原log170214B/SHA256 746f42b542f9d424b9fc2287238f925b2437290b72733e5ee0b95b2c6bd06043；原DEV语义JSON+LF17849B/SHA256 91aa9555dcfa17f2728e50ccffe7a9b7a7d5eca434a2861a1d1bda890bcb6b47。原REQUEST/DEV唯一、MODEL/COMPLETE不存在。原request35867B/hash6a7809a2…；其146项与原DEV140py闭包准确对应。

main先核本次实际146文件bytes。收据reader再确认原146路径集合相同，只有上述audit/dev两项可变，其他138py+6workflow hashes与当前request一致。由此复用的是实际原记录和未变依赖上的同一前三组，而不是把任意passed字样当新验证。

新增CURVATURE_GUARD_DEVELOPMENT_REUSE只输出源run/job、bytes/SHA、计数与范围；原收据payload只在runner内存和必要语义stdout，不入Git/artifact/Release。原scientific source仍唯一是covered run43762868037的真实375终态；多读的第二个日志仅用于已付14项，旧20/19/26/cache依然不执行。

## 后续唯一实际阶段

修改后的request仅编译这两份变更Python，先actual pull并查双README，再严格复用14、执行未完成4，成功后才进入这个guard算法的首次科学运行。仍从同一η=.2662701215525791、375-bank、4432/4451池、B=.00025、双streak0开始；12LP/40值/120秒active/每LP10秒全部原样。

这不是重复已完成科学阶段或增加预算：上一run在人工夹具处停止，没有新科学MODEL。若剩余接口仍失败，保具体失败并只处理它；若进入科学，保所有真实接受/拒绝、guard建模与started LP使用区别、原SOC/learning/两streak及完整费用。当前主题仍未完成。
