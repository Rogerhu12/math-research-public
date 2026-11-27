# R1130：原 inverse-center 和的完整 WZ 递推及相邻单位

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126。

**结论。** 对每个正奇整数 $n$，原有限和
$$
I_n=\sum_{j=0}^n\frac{(-1)^j\binom nj^2}{2j-n}
\tag{1130.1}
$$
满足准确的一阶非齐次恒等式
$$
\boxed{\quad
(n+2)^2I_{n+2}+16(n+1)^2I_n
 =4(3n+4)(-1)^{(n-1)/2}
       \binom{n}{(n-1)/2}.
\quad}
\tag{1130.2}
$$
在原 $p=3n+2\ge41$ 的素数情形，所有有限和都 $p$ 整，且
$$
\boxed{\quad
I_{n+2}+I_n
 =\frac92(-1)^{(n-1)/2}\binom{n}{(n-1)/2}
 \ne0\pmod p.
\quad}
\tag{1130.3}
$$
因此这两个准确相邻有限和不能同时为零。这里 $p$ 固定；
$I_{n+2}$ 只是同一公式的整指标邻项，不自动是原标签中的另一坐标。

R1059/R1061 原尺度仍为 $S_n=(2/3)I_n\pmod p$。
本篇**没有**证明 $I_n$ 或 $S_n$ 单独非零，也没有把
$I_{n+2}$ 换成原 $K_4$、primitive、Legendre 或其它 good 标签。
特定 $e,K_4$ 共同非零及主目标仍开放；后继须付真实邻项桥。

## 1. 精确符号证书与全部求和边界

本次运行只处理整指标 $n$ 的恒等式，没有重复一个素数窗口，
也没有从有限初值拟合递推。完整证书方法先见
[原请求说明](../notes/2026-11-27-original-inverse-center-wz-method.md)。

对本次实际找到的阶数二，令 $M=n+4$，
$$
Q(k)=(2k-n)(2k-n-2)(2k-n-4),\qquad
D(k)=(2k-n-2)(2k-n-4),
$$
$$
C_j(k)=
 \left(\prod_{h=1}^{2(2-j)}
       \frac{n+2j+h-k}{n+2j+h}\right)^2
       \quad(0\le j\le2).
$$
空积为一。附录的 $P(n,k)$ 及 $a_0,a_1,a_2$ 在
$\mathbf Q(n)[k]$ 中准确满足
$$
\begin{aligned}
&-(M-k)^2(2k-M)P(n,k+1)-k^2(2k-n)P(n,k)\\
&\qquad=\sum_{j=0}^2 a_j(n)C_j(k)
                      \frac{Q(k)}{2k-n-2j}.
\end{aligned}
\tag{1130.4}
$$
Actions 逐系数直接验证其残差为零；不是仅检验若干 $n,k$。
输出的 $a_j$ 与 $P$ 展开后均为整数系数多项式。
附录为了紧凑采用因式形式，其中表面上的分数必须先在
$\mathbf Q[n]$ 中合并；不能逐个把因式打印中的分母拿来模 $p$ 除法。

记
$$
H_M(k)=(-1)^k\binom Mk^2,\qquad
G(k)=\frac{k^2P(n,k)}{D(k)}H_M(k).
$$
由于
$$
\frac{H_M(k+1)}{H_M(k)}
 =-\frac{(M-k)^2}{(k+1)^2},\quad
D(k+1)=\frac{Q(k)}{2k-M},\quad
D(k)=\frac{Q(k)}{2k-n},
$$
(1130.4) 给出
$$
G(k+1)-G(k)
 =\sum_{j=0}^2a_j(n)
       \frac{(-1)^k\binom{n+2j}{k}^2}{2k-n-2j}.
\tag{1130.5}
$$
在 $n+2j<k\le M$ 时，$C_j(k)$ 分子有一个真正的零因子，
所以较短二项式项准确消失，不是把越界项作未证删减。

对任一正奇 $n$，$D(k)$ 在整数 $k$ 上无零；
$G(0)=G(M+1)=0$。故从 $k=0$ 到 $M$ 完整求和，得到
$$
a_0I_n+a_1I_{n+2}+a_2I_{n+4}=0.
\tag{1130.6}
$$
这里每个正整数专化所需的 $C_j$ 分母均非零。
清分母身份没有遗漏某一正奇指标。

实际三个 $a_j$ 的共同因子是
$$
\mathfrak c(n)=(n+2)(n+3)^2(n+4)^2.
$$
逐项除去这个正奇指标上非零的因子，得完整递推
$$
\begin{aligned}
&64(3n+10)(n+1)^2(n+2)I_n\\
&\quad+4(15n^4+152n^3+564n^2+900n+512)I_{n+2}\\
&\quad+(3n+4)(n+3)(n+4)^2 I_{n+4}=0.
\end{aligned}
\tag{1130.7}
$$
原未除因子的最高移位系数只有整数根 $-2,-3,-4$，
所以没有正奇指标上的向前递推退化。
在原 $p=3n+2\ge41$，$n+4<p$，上述共同因子及
$C_j$ 的分母也都是 $p$-单位。下面的单位结论只需 (1130.2)，
不依赖在模 $p$ 下逐次向前除最高移位系数。

## 2. Ore 算子的纸面因式分解

令 $E$ 表示步长二移位，$EI_n=I_{n+2}$。
系数与 $E$ 满足 $Ef(n)=f(n+2)E$。
(1130.7) 的算子准确分解为
$$
\boxed{\quad
L=\big((3n+4)(n+3)E+4(3n+10)(n+2)\big)
  \big((n+2)^2E+16(n+1)^2\big).
\quad}
\tag{1130.8}
$$
首末系数立即相合；中间系数的完整核对是
$$
\begin{aligned}
&16(3n+4)(n+3)^3+4(3n+10)(n+2)^3\\
&\qquad=4(15n^4+152n^3+564n^2+900n+512).
\end{aligned}
$$
这是根会话的纸面因式分解，之后由 o1 与 o2 独立复核；
没有在本地执行数学程序或只凭数值猜测。

置
$$
J_n=(n+2)^2I_{n+2}+16(n+1)^2I_n.
$$
外因子给
$$
(3n+4)(n+3)J_{n+2}
 +4(3n+10)(n+2)J_n=0.
\tag{1130.9}
$$
直接取原有限和的两个初值
$$
I_1=-2,\qquad I_3=52/3,\qquad J_1=28.
$$
若 $n=2m+1$，序列
$$
4(3n+4)(-1)^m\binom nm
$$
的相邻项比值为
$$
-\frac{4(3n+10)(n+2)}{(3n+4)(n+3)},
$$
并具有同一个初值 $28$。
(1130.9) 的系数在所有正奇指标上非零，
故完整一阶递推唯一性证明 (1130.2)。

## 3. 原素数专化与准确可消费范围

固定原 $p=3n+2\ge41$。因为 $n$ 与 $n+2$ 为奇数，
有限和的各分母均为非零奇数，绝对值至多 $n+2<p$；
所以 $I_n,I_{n+2}$ 的约化都合法。

(1130.2) 的右边约化为
$$
8(-1)^{(n-1)/2}\binom{n}{(n-1)/2},
$$
且 $n<p$ 保证该二项式为单位。
左边两个系数准确相等：
$$
(n+2)^2=16(n+1)^2=16/9\pmod p.
$$
这即给出 (1130.3)。

这是原 finite sum 的真实旁约束，包含所有因子。
原 $S_n=(2/3)I_n$ 的单独非零仍不能从一个相邻单位推出。
尤其没有付款以下任何一条替换：

- 将同一 $p$ 下的 $I_{n+2}$ 视为另一个素数的问题；
- 将它仅按权或长度对应到 $K_4$ 或某个实际 good 角色；
- 从递推的完备性推断原短主块的指定一列非零。

后继继续比较实际原函数、Cartier 矩阵和两指定 jet；
与已付相邻 $e_{\pm1}$ 的关系也必须逐尺度判断。

## 4. 公开执行、来源与小证书

本次唯一数学执行为公开仓库 GitHub Actions：

| 项目 | 实际记录 |
|---|---|
| source commit | 4a0f6f2106a32335d7d026d4168fe9f19d1e09ad |
| run / job | 46015627853 / 140561880424 |
| 结果 / 数学耗时 | success / 2.837720437999991 秒 |
| Sage | 10.6；官方固定 Docker digest |
| 预算 / reserve | 3600 / 90 秒 |
| 阶数一 | 6×5 精确矩阵；本请求范围中核维数零 |
| 阶数二 | 11×11 精确矩阵；完整证书，残差为零 |
| 阶数三 | 找到阶数二证书后停止，未运行 |
| 边界转录审计 | n=1,3,5,7,9,11 的完整有理有限和，全部通过 |

[真实 run](https://github.com/Rogerhu12/math-research-public/actions/runs/46015627853)
与 [真实 job](https://github.com/Rogerhu12/math-research-public/actions/runs/46015627853/job/140561880424)。

代码：[original_inverse_center_wz.py](../scripts/original_inverse_center_wz.py)。  
请求：[original-inverse-center-wz-request.json](../notes/original-inverse-center-wz-request.json)。

锁定的 Docker digest：
`sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879`。

- source SHA256：`e4765d302327bb6ca56ae14c1ccd3315e7cfe23fbf1b3b4783db912734e02fcd`
- request SHA256：`655c3f4e75ceaa91ab7e9cb39e8da263c517d747ac73f6f2080b310bfafe5078`
- certificate canonical SHA256：`9b8258335e8324b47dd398dd3f42039ad47f2926b8595822cbf920fee46b1c09`
- 根 README SHA256：`581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102`
- 课题 README SHA256：`6ce1403bd2d2587bb9cca70bd0095a1264b1167fe2c4b62f0652ae671e6277a5`

canonical certificate 为下列 JSON 的 sorted-key、无空白 ASCII 编码，
准确长度 1363 bytes。root/o1 亲读完整 job logs，各自重算文本 SHA 并一致。
有限六初值只核边界转录，统一证明来自 (1130.4) 的完整多项式证书。
不存可重算的大数组或 artifact。


```json
{
  "boundary_audit_odd_n": [
    1,
    3,
    5,
    7,
    9,
    11
  ],
  "boundary_audit_passed": true,
  "certificate_D": "product(2*k-n-2*j, j=1..order)",
  "certificate_G": "k^2*P(n,k)/D(n,k)*(-1)^k*binomial(n+2*order,k)^2",
  "certificate_P_coefficients_low_to_high": [
    "(255) * (n + 2) * (n + 3) * (n + 4)^2 * (n^4 + 2932/255*n^3 + 12389/255*n^2 + 22718/255*n + 5064/85)",
    "(-1776) * (n + 4) * (n^6 + 1933/111*n^5 + 55477/444*n^4 + 209755/444*n^3 + 440381/444*n^2 + 243157/222*n + 55114/111)",
    "(5226) * (n^6 + 47785/2613*n^5 + 5380/39*n^4 + 1434506/2613*n^3 + 244124/201*n^2 + 3696832/2613*n + 589760/871)",
    "(-8460) * (n^5 + 10702/705*n^4 + 192998/2115*n^3 + 114748/423*n^2 + 842536/2115*n + 54256/235)",
    "(8112) * (n + 10/3) * (n^3 + 1485/169*n^2 + 4272/169*n + 4018/169)",
    "(-4608) * (n + 5/2) * (n + 79/24) * (n + 10/3)",
    "(1440) * (n + 43/15) * (n + 10/3)",
    "(-192) * (n + 10/3)"
  ],
  "integer_coefficients": true,
  "leading_coefficient_integer_roots": [
    "-2",
    "-3",
    "-4"
  ],
  "nonvanishing_claim": false,
  "order": 2,
  "polynomial_identity": "exact_zero_in_QQ(n)[k]",
  "recurrence": [
    "(192) * (n + 10/3) * (n + 1)^2 * (n + 2)^2 * (n + 3)^2 * (n + 4)^2",
    "(60) * (n + 2) * (n + 3)^2 * (n + 4)^2 * (n^4 + 152/15*n^3 + 188/5*n^2 + 60*n + 512/15)",
    "(3) * (n + 4/3) * (n + 2) * (n + 3)^3 * (n + 4)^4"
  ],
  "scope": "all positive odd integers n after denominator clearing; leading-zero n retain the identity but not forward solving",
  "shift": 2
}
```

上述证书中 P 的数组按 k 的次数从低到高排列。
三项递推的化简、全部奇指标边界和 (1130.8)–(1130.3)
均由 root 与 o1 独立纸核；o2 另核算子展开、初值和一阶闭式。
本篇记录一条新的统一恒等式及旁单位，未声称主问题完成。


## 5. 同一个原和的准确短 Ramanujan 源

令 $n=2m+1$，并定义全为有理数的齐次归一因子
$$
\rho_m=(-16)^m\frac{(m!)^2}{(3/2)_m^2}.
$$
(1130.2) 还给出一个完整而保尺度的表示：
$$
\boxed{\quad
I_{2m+1}
 =-2\rho_m\sum_{j=0}^m
       (6j+1)\frac{(1/2)_j^3}{(j!)^3\,4^j}
 =-2\rho_m\sum_{j=0}^m
       (6j+1)\frac{\binom{2j}{j}^3}{256^j}.
\quad}
\tag{1130.10}
$$
这对全部整数 $m\ge0$ 成立，不只在模 $p$ 意义下成立。

为逐项证明，写 $A_m=I_{2m+1}$。齐次因子满足
$$
\frac{\rho_{m+1}}{\rho_m}
 =-\frac{64(m+1)^2}{(2m+3)^2}.
$$
将 (1130.2) 除以该因子并用
$\binom{2m+1}{m}=4^m(3/2)_m/(m+1)!$，得到
$$
\frac{A_{m+1}}{\rho_{m+1}}-\frac{A_m}{\rho_m}
 =-\frac{6m+7}{16\,4^m}
       \left(\frac{(3/2)_m}{(2)_m}\right)^3.
$$
换指标 $j=m+1$，右边准确变为
$$
-2(6j+1)\frac{(1/2)_j^3}{(j!)^3\,4^j}.
$$
初值 $A_0/\rho_0=-2$ 完成 (1130.10) 的全和，
而 $(1/2)_j/j!=\binom{2j}{j}/4^j$ 给第二种写法。

原素数情形现在是 $p=6m+5$；
$\rho_m$ 与所有显示分母均为 $p$-单位。因此
$$
S_{2m+1}
 =-\frac43\rho_m
    \sum_{j=0}^m(6j+1)\frac{\binom{2j}{j}^3}{256^j}
       \pmod p.
\tag{1130.11}
$$
这里仍是 R1059/R1061 同一原 $S$，不是重新定义一个旁标签。

### 5.1 截断点与完整微分边界

这个和的项属于经典 Ramanujan 型级数，
但本篇用的是 $m=(p-5)/6$ 的**实际短截断**。
Mao--Sun，
[Proof of a conjectural supercongruence modulo p⁵,
arXiv:2109.09877v1](https://arxiv.org/pdf/2109.09877)，
引言及 Theorem 1.1，处理的是上限 $(p-1)/2$；
root 已亲读原文。该结论不允许删除中间的尾段来证明 (1130.11)
的短和非零。此文献只标明同一项的已知来源与截断差别，
不作为本篇单位结论的输入。

同样，完整超几何级数的齐次微分方程在短截断上有明确边界。
令
$$
P_m(z)=\sum_{j=0}^m c_jz^j,\qquad
c_j=\frac{(1/2)_j^3}{(j!)^3},\qquad
\vartheta=z\,d/dz.
$$
逐系数准确有
$$
\boxed{\quad
\left(\vartheta^3-z(\vartheta+\tfrac12)^3\right)P_m(z)
 =-(m+\tfrac12)^3c_mz^{m+1}.
\quad}
\tag{1130.12}
$$
因为 $j^3c_j=(j-\tfrac12)^3c_{j-1}$，
所有 $1\le j\le m$ 的项抵消，剩下的就是显示的最后一项。
(1130.10) 的短和是
$((6\vartheta+1)P_m)(1/4)$。

在 $p=6m+5$ 时，$m+1/2=-1/3\pmod p$，
$c_m$ 也为单位；故 (1130.12) 的右边在 $z=1/4$ 非零。
这条原短输入不能直接套成无边界的完整 Clausen/Picard--Fuchs
齐次解。后继若沿该方向消元，必须保留这个强迫项及原
$S/e/K_4$ 的准确坐标桥。

root/o2 独立纸核 (1130.10) 的齐次因子、增量、初值、
central-binomial 因子及原截断整性；(1130.12) 为上述完整逐项证明。
没有新增数学程序执行，也没有重算已登记素数窗口。
