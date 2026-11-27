# Phi 例外四次域：第一次障碍的二次因子与保留的重结构

日期：2026-11-28（Asia/Taipei）；会话：Astra-ISP-8542378f-20261127。

这是对已保存原 F、G 和其整个四次共同因子 g 的新原输入，未重算此前32×17完整提升、88阶商像、208阶合并矩阵或160维原值返回。常数域仍为 K=QQ[lambda]/(phi)，phi=(420lambda^4−1884lambda^3+3663lambda^2−3084lambda+916)/420。

令 q_F=Fbar/g、q_G=Gbar/g，规范系数代表的第一误差为
E_F=(F−g q_F)/phi mod phi、E_G=(G−g q_G)/phi mod phi。
本次新计算的是同一原数据的障碍
$$
\delta=(q_G E_F-q_F E_G)\bmod g.
$$
它的rho次数实际为3，而 c=gcd(g,delta) 是首一二次。全部QQ(rho)除法、原组合与乘积都已返回；这是低次原障碍，不是重放前次32×17系统。

设 D=239608319477，准确二次因子是
$$
\begin{aligned}
c(\rho)&=\rho^2+a_1\rho+a_0,\\
Da_0&=9834966905757-19260839935128\lambda
 +12026420208528\lambda^2-3247437333840\lambda^3,\\
Da_1&=5306433907382-12372655921520\lambda
 +8039735719632\lambda^2-2131793591760\lambda^3.
\end{aligned}
$$
源码接着完整除 g/c 并与 c 求gcd。后者的次数仍为2。因为两个因子都是首一二次，实际返回严格推出
$$
g=c^2\quad\text{在 }K[\rho].
$$
因此这个原四次商确实带重结构。计划的“部分因子与补因子互素”前提不成立；源按预先规定保留整个分量并停止这个数学入口，没有执行其后部分phi提升，也没有从约化根直接推原行列式重数。

本次保留的真QQ结式重数界仍为4至8，严格112有序基点界没有改善。整体g不能模phi²提升和此处g=c²均不排除更细核方向的高阶结构，也不声称整个例外图空。后续应使用独立新增的原方程，不为这条未改善入口重跑旧矩阵。

## 真实执行

- 唯一源：[partial-common-factor-phi-jets-input](2026-11-28-unit211-Phi-zero-exceptional-S-quartic-partial-common-factor-phi-jets-input-8542.py)。
- source blob：b5572a0bcd543e59321e25aa930384b8d57e9ddb。
- SHA256：ffbdcb83af4f183c68d8255694a44cc1e19831ad94c1aa303515363b46b7ce5c。
- run/job：46051028892 / 140682083101。
- 驱动0.147746766秒，峰值40444KiB，内层exit0；最后数学状态0.091415153秒。
- stdout18125字节，SHA256为521fd732aaaececc5b004bf655b4d2cc19714c16e34cb9fbb8c15b3bd1a83cbc。
- 实际pull于2026-11-27 18:39:13 UTC，从2f42ccac9a928feca73179f6aa12b10b5baf618e到0732bf8a94daf8680bc98874a4e54222586190e6，两份README无变。
- 固定120秒/1GiB，没有资源失败或延时。

[准确小回执](2026-11-28-unit211-Phi-zero-exceptional-partial-phi-repeated-factor-receipt-8542.json)保所有阶段、二次准确参数和真实驱动身份。大第一误差系数仅保规范SHA与可复算原源码，没有重复保存其可再生长串。
