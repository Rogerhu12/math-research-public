# R852：原五个单 Z 系数的准确坐标与常数项 DAG

日期：2026-11-16。状态：执行方法；实际新坐标、秩及运行结果须由公开 Actions 的完成证书给出。本地没有运行本核。

## 1. 同一个原公式

直接消费 [ZA](2026-11-16-original-three-isogeny-sigma-and-one-Z-period-contraction.md) 的 (ZA.29)–(ZA.32)，该正式证明 SHA256 为
268fa3fbb9647d7f6f3f781534d9425e09c45ad7945e9aea9a9abd2082834d97。
固定原 $f=f_4$、$f(c_1)$、局部参数 $z=a-1$、$\omega=dx/(2y)$，
以及 $a=h_f$。五个原 $(p_j,q_j)$ 是
$(165,67),(93,67),(100,67),(168,67),(371,134)$。它们仍按原 R791 的
$r_j=p_j/q_j-2$ 及其来源记录绑定，不单凭这一数字表替换原对象。

令
$
c_j=\frac{y(T^jf)-y(f)}{x(T^jf)-x(f)},\qquad
C_j=3\left[(2-p_j/q_j)a+\rho_j\sigma^j(a)
+\sigma^{-j}(\rho_j^{-1}a)\right],
$
$
D_j=3c_j\left[a+\rho_j\sigma^j(a)\right].
\tag{852.1}
$
原椭圆一阶组合准确等于
$
3(B_{g_j}-p_jB_f/q_j)
=7\,\operatorname{tr}_{\chi,L}(C_jZ+D_j),\qquad
Z=\mathcal Z_b(f(c_1)),\quad
\operatorname{tr}_{\chi,L}=\frac{c_\chi}{14}
\operatorname{Tr}_{L_{41}/\mathbf Q_{41}}.
\tag{852.2}
$
外因子7、角色尺度、原十四次域和完整 $\rho$ 都保留。这里不把 $C_j$
移出 trace，不将 $T^7=\zeta^2$ 误写为 $T^7=1$，不以 (852.2)
替代 ZA.32 中的原 $Y$、Hecke 校准和全部非41项。

## 2. 新的准确小计算只需原 Hom 矩阵和十二切向

R791 的原整数矩阵 $C$ 是 $T$ 在十二个原 Hom 基中的作用，按列作用；
其准确来源已经证明 $C^{21}=I$、$C^7=J^2$，以及全部84个原域坐标的作用等式。
对任意原 Hom 字 $u$，切向映射满足
$
h(Tu)=\rho\,\sigma(h(u)).
$
这由 R791 的完整微分向量恒等式与原 $c_1$ 的六个有理 Hodge 一阶系数直接给出。
因此
$
\rho_j\sigma^j(a)=h(T^jf),\qquad
\sigma^{-j}(\rho_j^{-1}a)=h(T^{-j}f),
$
从而
$
\boxed{\quad
C_j=h\!\left(3\big[(2-p_j/q_j)I+T^j+T^{-j}\big]f\right).
\quad}
\tag{852.3}
$
负方向使用原 $T^{-j}=T^{21-j}$；并不丢掉七次绕回的 CM 相位。

$T^jf$ 的字已在 R844 点记录中，直接读取；只对新的负方向右端应用已成
$12\times12$ 矩阵。原 $C,J$、Hom 格、Gram、度数、原点加法和切向都不重建。
将 (852.3) 的十二个有理系数与 R791 十二个准确切向相乘、相加，得到
$
1,b,\ldots,b^6,\ \zeta,\zeta b,\ldots,\zeta b^6
$
中的十四个准确有理数。这一步不需要重新获得 $b$ 的最小多项式，
不做任何新域乘法，也不求四响应或原 $2420$ 系统。

同时对五个十四坐标列作准确有理消元，记录实际秩、选行和非零子式。
未运行前不预填秩5。若结果是秩5，则其意义只是五个 $C_j$ 作为原域元素的
$\mathbf Q$ 线性独立；它不证明五个 trace 值、完整高度或高度行列式非零。

## 3. 原 733 节点完整继承

新程序首先核 R844 的529个节点逐字等于 R846 的733个节点的前缀，
再原样导入全部733个节点。旧 ID、payload、proof、configuration 一律保留。
采用冻结 R841 的内容寻址 Program 和 Source 类；不调用其旧数学 Job。

五个 $c_j$ 是 R844 原 secant 的既存节点。其分母及逆节点已经由同一点的
非挠性与原不同、非相反 Hom 字证明非零，本次按旧 payload 精确找到它们，
不重复点加法或创建新的 inverse。原 $\rho_j^{-1}$ 也直接复用原逆节点。

$h_{g_j}$ 已在 R846 的原一阶程序中，因此
$
D_j=3c_jh_{g_j}
\tag{852.4}
$
只需新的标量乘法节点。$D_j$ 中仍包含原 unit-chart 的四个响应，
所以这次只输出它的准确表达式，不称已展开原有理点坐标。

程序还保 (852.1) 中完整 $\sigma$ 表达式的 $C_j$ 根及 (852.3) 的 Hom
线性组合根，两者的等值依据绑定原 R791 作用证书和 ZA 正式证明。
新 $\sigma^k$ 节点沿 R846 的相同语义作用于整个准确表达式及所有原常数，
固定原 $\zeta$，不能只共轭 $b$ 而保留未共轭响应。

新逆节点数和新点加法数均为零。实际新节点数须读取完成产物，
不在本地执行构图来预报它。

## 4. 真实源、最小载体与身份

唯一直接来源是已成功 R847：
run 43789012126、source f699023d15daacb7d7e176f52da41899d69ae26c，
artifact 14191283725；
原 archive 为11198983 bytes，SHA256
1737c833763f617e192447f1656d6793cd6d7eb6b78dfdbac0e4d8a9192aac98。

从该原 manifest 精确选九件：manifest/reference、run/core/input receipts、
完成证书、source-audit、原 retained receipt 和原输入包。选择身份沿
已成 R850 的同一 POINTS 选项，不取 R847 的1413个旧球阶段。
原输入包2078830 bytes，SHA256
a7ccfe9b61d59233e622505afd0a664e18be8d1384a093b446b8b02bf7b9ddb1，
完整270个成员分属 CM、DAG、JETS、NONTORSION、POINTS、R791。
逐成员验证其原 manifest、完成 tag、来源 run 和父子身份。

wrapper 直接调用冻结 R850 stdlib transport 的实际 POINTS 函数与 R824
Range helper，不重设旧模块的 RESULT、LABELS、core 或数学 tag。
仅九件直接成员封装成新的一日必要载体，270件原叶已在其中。
不下载395MB GLOBAL，不重旧 Hensel、Dixon、非挠、Hom 或一阶见证。

Range 传输所称 archive SHA 是原 GitHub API 所给 SHA 及被选成员的真实 SHA；
没有声称在本地重哈希完整原 ZIP。只有读过的原成员才能称已核。

## 5. 完成、续算与边界

数学核心分三阶段：原来源 audit、准确系数/常数项程序、五个 $C_j$ 的准确
十四坐标及有理秩子式。每阶段写完原子 rename，保完整配置和 SHA。
预算不进入数学身份；真正恢复只消费同 tag 的完整阶段。
wrapper 总是写真实 core/run 退出码与完整输出 manifest，不用缺失证书假装成功。
一日 artifact 只保当前输入、完整数学阶段及必要 continuation；机器值不进 Git 或 Release。

本次成功必须明确：
五个 $C_j$ 准确展开；五个 $D_j$ 是原准确 DAG；原733节点、全共轭、
相位、外因子7和角色尺度不变。
以下仍为 false：实际41四响应球、实际 $Z$、展开的 $D_j$、原 $Y$ period、
原高度、A.1 准确零、全素数一致性。
后继 R854/41C 可消费这些准确系数和原节点，但必须自行取得真实41球、
分母赋值及全部解析尾；任何辅助素数的旧球都不代41数值。
