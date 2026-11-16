# 完整 cap5 有理积分证书：唯一新任务

日期：2026-11-16。设计见 [完整五门设计](complete-cap5-integral-positive-certificate-design-20261116.md)。这是原五条完整门的新多项式证书问题；旧十五参数、三原子和四原子搜索均已闭账，不读旧搜索输出，不重新求值。

## 冻结的数学问题

保 $H\in[3/5,67/36]$、$C=(H-3/5)\zeta$ 与 $0\le\zeta\le1$，不在 $H=3/5$ 除法。原十二项密度、八个同锚累计量和五条 $80H^3\Delta_\nu$ 全保。端势固定为设计中85项、九个已证明非负生成元及全部规定的参数/空间次数，包含真实 $C$ 尾和 $A_f$ 余项。只有一次 LP，没有自适应分区、改次数、扩池、改变有理化网格或重启。

浮点 LP 只给一个候选；按固定 $2^{-40}$ 网格有理化后，从未缩放的 Fraction 原列重建所有余式。每一个负 Bernstein 残系数都以设计的真实积分上界扣损，成功只认精确有理不等式
$$
E_{\min}>D_A+D_Q.
$$
LP status、浮点 epsilon 和有限 ansatz 失败均不解决真实 cap 类。若得到严格证书，它排除的是这套完整五门的 cap 类，不能冒充主课题一般曲面的不存在证明。

## 源与账户

新入口 [complete_cap5_integral_certificate.py](../scripts/complete_cap5_integral_certificate.py) 为40,404字节，SHA256 `86a98b92d29c2c3fd4f394adf06c39d4f9441096a504e0daf45e37f934b1e0e6`。人读设计14069字节，SHA256 `56003d874582e927787b7051cfbeb4de157bc0d056720f161ea1ce5f9b28c0c5`。固定请求 [request-complete-cap5-integral-certificate.json](../computations/request-complete-cap5-integral-certificate.json) 的 SHA256 为 `27f9e118eece47cbf30426efab32feb1a3517975084918e6cc2ea6f7a2be4756`，实际 source commit/run/job 由唯一公开 Actions 记录。

新总钟600秒；唯一 LP 最多180秒，LP 后预留180秒供唯一精确 judge。全部输入、导入、系数组装、LP、失败、有理重构、输出均由入口总钟计，不把 nested 段重复相加。静态组合上界59,405变量、82,650系数行、6,483,518未合并entries只是源形式上界，没有运行预检；固定上限分别60000、85000、7000000。完整 stdout 上限40MiB，另在其内给最后账留256KiB。

首次执行前仅调整草稿的三个时间数为上述600/180/180，所有数学池/次数/域/舍入网格原样。此前没有执行、导入、编译或测试本科学入口。

## 执行与输出

工作流 `.github/workflows/visible-complete-cap5-integral-certificate.yml` 对请求文件的一次推送触发；研究与只读报告 job 均先真正拉公开/私有仓库，逐次检查双 README，只输出差异与规则身份，私有令牌在科学入口前移除。实际 source detach 后使用已公开源/请求；不跑旧研究或开发检查。

原返回的所有非零浮点系数以 binary64 hex 记入原 stdout；有理系数、全部完整余式、端点与精确 judge 也各自有完整原记录。只读报告仅复制语义结果、费用、身份及实际 pull，不重算 LP 或证书；大系数数组仍在原 stdout，报告身份不是可重用数值缓存。机器输出只在公开原 stdout 和临时 runner，不上传 artifact/Release/cache，不写 Git。

此条只冻结并提交唯一新任务，尚无科学结果。得到实际 LP/judge/最终钟后立即登记并继续 open；预算用尽不会被写成课题完成。
