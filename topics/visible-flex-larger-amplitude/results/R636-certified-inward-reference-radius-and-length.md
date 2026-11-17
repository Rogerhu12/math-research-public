# R636：内向参考端半径与径线长度的严格积分包围

作者：Astra-larger-parallel-16f63c8b（GPT-6 Astra Pro，AI辅助），2026-11-17。

**已证明；结清 R634 的两个参考积分条件。** 对已登记的 .995 真父对应的内向参考设计，曲率平台为 \(3/2\)，首尾过渡长度均取保存的 IEEE .02，以显示曲率及**精确位置积分**定义参考曲线，则

$$
.53187889470968<R<.53187892868261,\qquad
1.28971664673515<L_g<1.28971664673518.
\tag{1}
$$

因此该参考设计满足 [R634](R634-inward-fixed-material-full-angle-chord-budget.md) 此前未认证的 \(R\in[.531878,.531880]\)、\(L_g\ge1.289716\) 两条件。同一真实 .995 cut 的全部112模、同一材料对应和目标高度 \(H=9/5\) 遂满足

$$
\sup_\phi |T_R(\phi)-F_b(\phi)|<1.229702,\qquad
L_g-\sup_\phi |T_R(\phi)-F_b(\phi)|>.06001464673515.
\tag{2}
$$

这是指定端点的长度必要门。没有构造实际非轴尾、支付实际末端 jets、闭面或 reach，也没有把参考高度增量冒成实际非轴场的末高。

## 1. 对象、精确参数及起点记录

完整真实父 parallel-continue0995-m112.json.gz 的 SHA256 为

~~~text
d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f
~~~

既有 [inward_profile.py](../scripts/parallel_20261117_inward_profile.py) 明确规定：数学对象由曲率和精确 meridian 积分定义；有限 Gauss32 只是评价器。本条认证该数学对象的 \(R,L_g\)，不宣称有限 Gauss 表达式的逐字导数自动等于分别返回的 \(a',a''\)，也未认证该评价器在全域的误差。

恒曲率解析段始于保存的 .99。原几何最后精确有理节点显示为

$$
(a_0,v_0,u_0)=(1.1666064106120295,\ .357948638910307,\ -2.0101206107275877).
$$

每个显示值代表源 JSON 的 IEEE 数，再精确转为有理数。原数值 Profile 从同一五次式算出的起点常数仅在速度上略异，为 .3579486389103069。为同时覆盖精确节点定义和已记录起点常数，采用独立有理盒：

| 参数 | 下界 | 上界 |
|---|---:|---:|
| \(a_0\) | 1.16660641061202 | 1.16660641061204 |
| \(v_0\) | .35794863891029 | .35794863891032 |
| \(u_0\) | −2.01012061072760 | −2.01012061072757 |

完整源逐个用精确有理数验证两份记录均在盒内。下面结论对盒内**每一组三参数**成立，故不依赖选择哪份起点记录。各组的理想恒曲率延拓定义为

$$
K=-\frac{u_0}{\sqrt{1-v_0^2}},\quad
\alpha_b=\arcsin v_0,\quad
\alpha_c=\alpha_b-K(s_c-s_b),\quad
a_c=a_0+\frac{\cos\alpha_c-\cos\alpha_b}{K}.
\tag{3}
$$

保存的曲率2.15275972133223也在 (3) 的严格区间内。本次精确参数为

$$
s_b=\frac{4458563631096791}{4503599627370496},\quad
s_c=\frac{8962163258467287}{9007199254740992},\quad
h_i=h_o=\frac{5764607523034235}{288230376151711744}.
\tag{4}
$$

区间计算给 \(2.152759721332196<K<2.152759721332255\)、
\(.355306240521157<\alpha_c<.355306240521191\)。故
\(\arcsin(\sin\alpha_c)=\alpha_c\)；理想 inward 定义由 \(a'_c\) 恢复角度、由 \(a''_c\) 恢复曲率，与 (3) 一致。

## 2. 三段曲率与精确长度

记

$$
S(u)=10u^3-15u^4+6u^5,\quad
P(u)=\frac52u^4-3u^5+u^6,\quad k=\frac32.
$$

有 \(P'=S\)、\(P(1)=1/2\)，且 \(0\le S\le1\)、
\(0\le S'(u)=30u^2(1-u)^2\le15/8\)。首末过渡角度分别为

$$
\alpha_i(u)=\alpha_c-h_i\{K(u-P(u))+kP(u)\},\qquad
\alpha_o(u)=\alpha_2-kh_o\{u-P(u)\}.
\tag{5}
$$

首段末角、平台末角及平台长度为

$$
\alpha_1=\alpha_c-\frac{h_i(K+k)}2,\quad
\alpha_2=-\frac\pi2+\frac{kh_o}2,\quad
\ell=\frac{\alpha_1-\alpha_2}{k}>0.
\tag{6}
$$

三段曲率是 \(K+(k-K)S\)、\(k\)、\(k(1-S)\)，在接缝匹配；末角恰为 \(-\pi/2\)，末曲率为0。精确长度是 \(L_g=h_i+\ell+h_o\)。由 (3)–(6) 得

$$
\frac{1289716646735154676755027}{10^{24}}
\le L_g\le
\frac{1289716646735176682398240}{10^{24}}.
\tag{7}
$$

这蕴含 (1) 的长度界，不使用位置求积。

## 3. 半径积分与显式余项

半径公式为

$$
R=a_c+h_i\int_0^1\sin\alpha_i(u)\,du+
\frac{\cos\alpha_2-\cos\alpha_1}{k}
+h_o\int_0^1\sin\alpha_o(u)\,du.
\tag{8}
$$

仅两个短 ramp 需要积分。沿实际弧长变量 \(t\)，\(\alpha'=-\kappa\)，故

$$
|(\sin\alpha)''|,\ |(\cos\alpha)''|\le\kappa^2+|\kappa'|.
$$

利用 \(K<2.153\)、\(0<K-k<.653\)、\(S'\le15/8\)，可以取

$$
M_i=(2.153)^2+\frac{.653}{h_i}\frac{15}{8},\qquad
M_o=k^2+\frac{k}{h_o}\frac{15}{8}.
$$

每段64个等长中点区间的复合中点误差严格不超过

$$
E_i=\frac{h_i^3M_i}{24\cdot64^2},\quad
E_o=\frac{h_o^3M_o}{24\cdot64^2},\quad
E_i+E_o<1.698643\times10^{-8}.
\tag{9}
$$

(9) 支付完整区间之间的误差，不以两种求积阶数吻合替代余项。对 (8) 向外求和并加 (9)，得到

$$
\frac{531878894709684074185788}{10^{24}}
\le R\le
\frac{531878928682601659199831}{10^{24}},
\tag{10}
$$

从而 (1) 半径界成立。同法还给
\(.89449825549622<\Delta z_{\rm ref}<.89449828946910\)。
它是参考曲线的增量；(2) 中的1.8仍是指定非轴圆端点高度。

## 4. 算术与复现

全部区间在 \(10^{-24}\) 格点上以 Python 整数/Fraction 向外舍入。平方根由整数 isqrt 给下界及向上取整的上界，正分母除法取四个端点商的最小与最大值。起点 arcsin 使用32个正项

$$
\sum_{j=0}^{31}\frac{\binom{2j}{j}}{4^j(2j+1)}x^{2j+1}
$$

及余项上界 \(x^{65}/(1-x^2)\)：所有系数至多1，且 \(0<x<1\)。上下输入端点可分别给上下界。

\(\pi\) 沿用 R634 的64项 Machin 包围；sin/cos 使用同一冻结的96/97阶 Taylor 整数区间、一个格点余项并支付输入角区间半径。全部角在其 \(|x|\le10\) 范围内。不使用浮点三角函数、平方根或 Gauss 输出作为严格界。报告浮点数只供显示。

源 [2026-11-17-parallel-inward-integral-enclosure.py](../notes/2026-11-17-parallel-inward-integral-enclosure.py)，SHA256：

~~~text
babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0
~~~

唯一三角辅助源为 R634 的 inward-chord-cover.py，SHA256：

~~~text
e480a2ca7ebd5911768cad04ef7b98319ff2cff1840cf71531eaf2b574b4211a
~~~

~~~sh
PYTHONDONTWRITEBYTECODE=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-inward-integral-enclosure.py \
  --input /scratch/parallel-continue0995-m112.json.gz \
  --out /scratch/parallel-inward-integral-enclosure.json
~~~

/scratch 换成实际仓库外目录。默认每段64个中点，不依赖 NumPy/SciPy；原父及报告不入库；本次报告SHA256为 1e08c3cbc17755de01bca9a97065ad93f0dbdd7ac25f3392d8fc11741ab7b9d5。原参考实现 SHA 为 1816ba9f5c9d1c207ba5e502ed5fa37a2f28807c54067cde766ae313df40e3e0，本条未修改它或任何 BVP。

(1) 与 R634 共同证明 (2)。必要长度门不蕴含非线性尾存在，等距闭合、实际 C² 接缝、完整D、held、含反射商距离、全t嵌入与reach仍须实际支付。
