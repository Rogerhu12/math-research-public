# R810 — 原 r=2 四次因子的完整零角、全最大子式与全素数强窗排除

日期：2026-11-15。**状态：下述原 Fp、r=2、b=4、b0=3 强接触窗口的全素数排除已证明。结合 R799/R803，原这个窗口的任何剩余因子必须 b≥5；不据固定次数排除推广到随 p 增长的次数，原同一个 R 的完整提升仍开。**

本篇保原十九角、真实低轴、全部常数 charge 系数以及强门。
四次因子的零角四步重数为 (1,0,0,0)，其第四个系数带真实 t 因子。
这两处是本篇相对三次证明的实际变化，不能只改旧脚本的求和上限。

## 1. 原范围与不变的实际低轴

设
$$
p=12h+11=6s-1>101,\qquad s=2h+2,\qquad
k_{\rm carry}=0,\quad r=2,\quad f_D<p,
$$
$$
P^{\rm fact}=qt^2F^3\in\overline{\mathcal W}_D,\qquad
F\in\mathbf F_p[t,Y],\quad b=\deg_YF=4,\quad
b_0=\deg_YF(0,Y)=3.
\tag{1}
$$
F 是原 primitive 不可约因子，保
$$
F(0,1)=0,\quad F_Y(0,1)\ne0,\quad q(0,1)\ne0.
$$
令 C 为同一个十九次吹起曲面上的严格变换，
$$
\kappa=C^2,\qquad \chi=-K_XC.
$$
本篇只使用原强门
$$
\boxed{\operatorname{ord}_tF(t,\rho(t))\ge h,\qquad h\ge\kappa+14.}
\tag{2}
$$
这里
$$
d=1+8t,\qquad h_7=7+4t+16t^2,\qquad
\rho=d\Theta^{17},
$$
$$
\Theta(t)=\exp\!\left(
 \sum_{n\ge1}\frac1{3n}\frac{(1/3)_n}{(5/6)_n}t^n
\right).
\tag{3}
$$
在严格低于 s 的原窗口，(3)就是原 regularized 低轴。
本篇读取的每个有限矩阵只到 h−1<s，不把它替代真正高尾或下一位。

**定理。** (1)–(2) 不存在解。结论同时覆盖 q(t,0) 为零与非零。
在原允许的两个 ell 窗口中，只要上述同一 p/h 关系和强门成立，结论同样成立；
证明不使用 ell=1 独有的第三块运输。

## 2. 两种常数 charge 的统一必要包络

R792/R797 已给全部常数项分类：
$$
F(t,0)=\lambda d^cH(t),\qquad
c\ge0,\quad H\text{ monic},\quad z=\deg H\in\{0,1,2\},
\quad (H,d)=1.
\tag{4}
$$
允许 H(0)=0；所有低 H 系数都是实际未知列。

当 q(t,0)=0 时，原 r=2 窗口迫
$$
q=Y\widetilde q,\quad m_q=1.
$$
其 mask 为
$$
A=(t-1)^i d^j h_7^k,\qquad i+j+2k\le6-3z.
\tag{5}
$$
原始 mask 数量分别为50、13、1。
对 (5)，四次因子的亏损上界是
$$
m_h\le \min\!\left(4,\left\lfloor\frac{4k+1}{3}\right\rfloor\right),
\quad m_1\le\min(4,i),
$$
$$
\delta_d\le\left\lfloor\frac{2j+1}{3}\right\rfloor,\qquad
2z\le\delta_\infty\le
 \left\lfloor\frac{13-2(i+j+2k)}3\right\rfloor.
\tag{6}
$$
与三次情形不同，m_h、m_1 的 degree 上限是4。
按 (z,m_h^{max},m_1^{max},delta_d^{max},delta_inf^{max}) 去重，
这次准确得到57个包络。

当 q(t,0)≠0 时，R792 不加 m_q=0 便给 z=0 及 R782 的五型。
它们包含在 (5) 的以下 z=0 包络中：

| 原五型 | 原上界 (mh,m1,dd,di) | 所用 (5) 的 mask |
| --- | --- | --- |
| 1 | (0,0,0,1) | 1 |
| t−1 | (0,1,0,0) | t−1 |
| (t−1)^2 | (0,2,0,0) | (t−1)^2 |
| h7 | (2,0,0,0) | h7^2 |
| d^2 | (0,0,1,0) | d^2 |

这是必要包络的包含，不是替换旧 q 或原因子的几何类。
尤其 h7 型的 mh 上界是2；采用 h7^2 包络只将上界放宽到3。
下文对实际重数与实际 κ、χ 再逐类筛选。

令 G=F/(lambda d^c)，所以 G(t,0)=H。
对一个包络及 1≤n≤4，全部正 charge 系数为
$$
G_n=t^{a_n}h_7^{b_n}(t-1)^{c_n}d^{-z_n}p_n(t),
$$
$$
a_n=\left\lfloor n/4\right\rfloor,\quad
b_n=\max(0,\lceil(n-m_h)/4\rceil),\quad
c_n=\max(0,\lceil(n-m_1)/3\rceil),
$$
$$
z_n=\lfloor(n+\delta_d)/2\rfloor,\quad
K_n=\lfloor(9n+\delta_\infty)/2\rfloor,\quad
\deg p_n\le E_n=K_n+z_n-a_n-2b_n-c_n.
\tag{7}
$$
这些式子逐条来自原 Gauss 帽。特别 a4=1，前三个 an=0。
在 rho 上的全部列为
$$
t^{a_n+j}h_7^{b_n}(t-1)^{c_n}d^{n-z_n}\Theta^{17n},
\qquad 0\le j\le E_n.
\tag{8}
$$
再加常数 charge 的全部列 1,t,…,t^(z−1)，右端为 −t^z。
原 H 的零根、移动根和低系数均未删除。

## 3. 57个完整有理矩阵与所有大素数

对每个 (7)，记正 charge 列数为 N。
加入 1,t,…,t^z 后的整个 augmented 矩阵有 N+z+1 列。
在行0,…,z中，后 z+1 列组成恒等块；
在行>z中，这些列为零。因此任一非零全列最大子式必须包含行0,…,z，
其余部分就是 (8) 的 N 阶子式。

公开 producer 从 (3) 的有理递推重建到第96行，
先取两个相邻行区间的精确最大子式，再对所用完整行块作整数 Hermite 正规形。
每行只乘该行原有理系数分母的最小公倍数。
对完整 post-pivot 行块 A，满列秩 HNF 的非零对角元乘积
$$
\boxed{\Delta(A)=\gcd\{\text{A 的全部 N 阶子式}\}}
\tag{9}
$$
是实际全部最大子式的 gcd，而非只取某个非零行列式的高度。
所用行块、两子式区间、流 hash、完整 gcd 因式和输入规则均在公开输出中列明。
常数块行的清分母因子只影响同一有限小素数集合。

准确执行结果是：
$$
\boxed{
\text{全部57格满列秩，最高使用行为50，全部 }\Delta(A)
\text{ 的素因子不超过283。}}
\tag{10}
$$
每格两个相邻最大子式及 HNF 都来自同一个完整 (8)。
既有列未删除，不用模 p 秩来猜特征零秩。

到第 i 行的 (3) 分母，仅由 i!、各 n≤i 及 6n−1 的素因子组成。
因此所有所用行的分母素因子不超过299。
由 (9)–(10)，若
$$
\boxed{p>611,}
\tag{11}
$$
则 p 不整除行分母或完整最大子式 gcd，而 h=(p−11)/12>50。
所以原接触前缀已含一个满列秩单位子式。
这排除所有 (7) 的非齐次系统，进而排除所有满足 (1)–(2) 的因子。

(11)没有有限扫描外推：57个有理证书及其完整素因子分解，
直接支付每一个大于611的目标素数。

## 4. 小素数的真实十九角类：新增零角不能漏计

下面在同一个原曲面上枚举剩余的必要几何类。
零角四步总重数为
$$
b-m_F=4-3=1,
$$
且重数不增。因此唯一可能是
$$
\boxed{\boldsymbol\mu_0=(1,0,0,0).}
\tag{12}
$$
它在自交数中贡献1。其累计重数均为1，
逐 charge 的条件给 a_n=floor(n/4)，正是 (7) 中的真实 t 因子。

因 p≡5 mod6，h7 在 Fp 上不可约，其两个几何链的重数相同。
取每个包络中所有实际
mh、m1、dd、di，并令
$$
v_d=2c-\delta_d,\qquad
v_\infty=2v-\delta_\infty,\qquad u=c+v.
$$
primitive 性及真实径向次数给
$$
0\le v_d,v_\infty\le4,\qquad
0\le c\le\lfloor(4+\delta_d)/2\rfloor,\qquad
z\le v\le\lfloor(4+\delta_\infty)/2\rfloor.
\tag{13}
$$
取所有非负不增重数序列
$$
\begin{array}{c|c|c}
\text{链}&\text{长度}&\text{重数和}\\ \hline
\mu_h&4&4-m_h\\
\mu_1&3&4-m_1\\
\mu_d&2&v_d\\
\mu_\infty&2&v_\infty.
\end{array}
\tag{14}
$$
每项不超过4。H 的全部常数项条件还要求
$$
\mu_{d,1}\le c,\qquad \mu_{\infty,1}\le v-z,
$$
$$
V_j^d\le jc,\qquad V_j^\infty\le j(v-z)
\quad(j=1,2),
\tag{15}
$$
其中 Vj 是相应累计重数。

原曲线除子类为
4Σ+(u+16)f 减去全部十九个实际重数。
由 (12)–(14)，准确得到
$$
\boxed{
\kappa=64+8u-1-2\sum\mu_h^2
                 -\sum(\mu_1^2+\mu_d^2+\mu_\infty^2),}
\tag{16}
$$
$$
\boxed{\chi=11+2m_h+m_1+\delta_d+\delta_\infty.}
\tag{17}
$$
−1就是不能遗漏的零角平方和。保留
kappa≥chi−2 及 kappa−chi 为偶数，这只是必要的属条件；
没有假定线性包络自动含有不可约曲线。

还可直接核得
$$
\boxed{\kappa\ge15+8z.}
\tag{18}
$$
事实上 2Σmu_h²+Σmu_1²≤48。
由 (13)、(15)，Σmu_d²≤4c、Σmu_inf²≤4(v−z)，
代入 (16) 得 kappa≥15+4c+4v+4z≥15+8z。

对每个这样的实际类，正 charge 系数的完整帽为
$$
F_n=t^{a_n}h_7^{b_n}(t-1)^{c_n}d^{z_n}p_n,
\qquad 1\le n\le4,
$$
$$
a_n=\max\left(0,\max_{j\le4}
 \left\lceil\frac{1-4+n}{j}\right\rceil\right)=\lfloor n/4\rfloor,
$$
$$
b_n=\max\left(0,\max_{j\le4}
 \left\lceil\frac{V_j^h-4+n}{j}\right\rceil\right),\quad
c_n=\max\left(0,\max_{j\le3}
 \left\lceil\frac{V_j^1-4+n}{j}\right\rceil\right),
$$
$$
z_n=\max\left(0,\max_{j\le2}
 \left\lceil\frac{V_j^d-n}{j}\right\rceil\right),
$$
$$
K_n=\min\left(u+4n,\min_{j\le2}
 \left\lfloor\frac{ju+(4j+1)n-V_j^\infty}{j}\right\rfloor\right),
\quad
\deg p_n\le K_n-a_n-2b_n-c_n-z_n.
\tag{19}
$$
(19)保完整链的每个中心，不只使用最后一个 Gauss 值。

全部评价列为
t^(a_n+j) h7^b_n (t−1)^c_n d^(z_n+n) Θ^(17n)。
另加 d^c t^j (0≤j<z) 的实际未知列；
右端准确是 −d^c t^z，读取全部0≤i<h行。
这没有将 H 的低系数当参数固定，也没有另选一个便于无解的来源。

(13)–(17)的有限嵌套枚举去重后共有10898个必要类。
这里只用它们的必要包络；进一步的不可约、精确角达到或 smooth 开条件
只会删除候选，不能制造新解。

## 5. 所有剩余素数和完整非齐次系统

由 (2)、(18)，h≥29。
在101<p≤611、p≡11 mod12的23个素数中，前11个均无满足强门的几何类。
其余全部必要系统如下：

| p | h | 满足 kappa+14≤h 的全部几何类数 | 相容类数 |
| ---: | ---: | ---: | ---: |
| 359 | 29 | 1 | 0 |
| 383 | 31 | 1 | 0 |
| 419 | 34 | 1 | 0 |
| 431 | 35 | 4 | 0 |
| 443 | 36 | 7 | 0 |
| 467 | 38 | 13 | 0 |
| 479 | 39 | 14 | 0 |
| 491 | 40 | 17 | 0 |
| 503 | 41 | 24 | 0 |
| 563 | 46 | 103 | 0 |
| 587 | 48 | 153 | 0 |
| 599 | 49 | 201 | 0 |

一共539个类的出现，去重后为438个不同的原非齐次矩阵。
每个矩阵在实际 Fp 上的 augmented 秩都比系数秩大一。
因此这里不需要再用 smooth、b0=3 或 (H,d)=1 的开条件删解。
与 (11) 合并，证明定理。

producer 枚举所有23个素数，而不是先只挑表中有候选的12个；
并保存所有输入的整合 hash。因此“前11个没有候选”也在同一确定性算法中核对。
全部枚举上界来自 (13)–(15)，不是经验截断。

## 6. 完整公开执行记录

数学运算全部在本库公开 GitHub Actions；没有本地或 V8 数学执行，
没有保存可重算输出数据文件。

- producer：[check-r810-original-r2-quartic-full-profiles.py](../scripts/check-r810-original-r2-quartic-full-profiles.py)；
- source commit：2a6ce4bd7a2ea78f55e94dcee1f9b5cf5829db0d；
- 参数：--max-order 96 --remaining-examples 12；
- python-flint：0.9.0；
- [run43746804944](https://github.com/Rogerhu12/math-research-public/actions/runs/43746804944)，job132911796266，退出码0；
- script SHA256：5ef0b926d54638a35ab53f50b1ed584f6bcff2a1472b9c8c6ca1cccbafee6600；
- stdout：29014 bytes，SHA256：d2efb68aa2995942cc8140f9618e2abfb33d769242073e98c747d33b42f428ae；
- 原 R788 精确运算 helper SHA256：f729371aa6867a84e1a4de18abdcd6d2451987e7174809a0a19269631c68da0e。

公开结果的57行 profile 表逐项给 mask、完整亏损、列数、两子式区间、
整 HNF 行区间/秩、全部 gcd 因式及 selected/full gcd 各自 hash。
主域为 uniform_gate_paid=true、largest_common_bad_prime=283、
largest_used_row=50、all_strong_b4_excluded=true。

完整 profile 报告 hash：
9e3bdd63c832dc6b1d85a3ce3ca9fe8258185c317e88345336478ac78dc03a15。

全部十九角几何输入 hash：
f7bd0b3df0ac53f584deb4082ca06db93ea77b197065cb51ba4383a52a534fc5。

全部实际有限矩阵及结果 hash：
42d43e2193006cfd0249d229d9807b7968d1034cb1d070862fe6064270342ff9。

全部有限素数报告 hash：
a4ef8e88114f253aa30993984e8c28543656fdd4db56c1bfa77b0837fd579fde。

这些 hash 是公开复现入口，不代替 (5)–(19) 对原来源、几何类和全部列的说明。
也不把本次 HNF 中的固定次数现象提升为一般 b 的最大子式公式。

## 7. 对当前主线的准确推进

R799/R803已排原 r=2 的全部 b=3 情形；本篇排 b=4。
因此在这里的原 Fp 强窗中，无论 q 的常数 charge 是否为零，
$$
\boxed{b\ge5.}
$$
所用全部矩阵、p/h关系与强门不含 ell，
所以这个必要排除不需借用 ell=1 的 lifting 公式便覆盖两个原 ell 窗口。

本篇不改变原已经固定的 P2，不以包络中的另一个 cube 替换同一个 R，
不删除 R790 的低除 p 商、完整 normal、两条十三行或 p³ 全高尾。
固定 b 的有限排除也不解决 b随p增长时的统一接触问题。
主目标仍未完成，继续原指定 forcing 与真正中央非消失。

依赖：
[R782](R782-original-r2-five-profile-factor-and-inhomogeneous-contact-gate.md)；
[R792](R792-original-nonzero-constant-charge-classification-and-cubic-extension.md)；
[R797](R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)；
[R799](R799-original-all-cubic-nonzero-constant-charge-windows-excluded.md)；
[R803](R803-original-zero-constant-cubic-all-prime-exclusion-and-full-r2-window.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)。
