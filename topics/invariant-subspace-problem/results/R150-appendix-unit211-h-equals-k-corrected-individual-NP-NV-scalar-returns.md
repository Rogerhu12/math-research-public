# R150 补充：h=k 的四个完整个别 N/P 条件与不除斜率的原标量返回

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 已完成的原必要条件

沿[正确五原行与三物理条件](R150-appendix-unit211-h-equals-k-corrected-five-original-rows-and-three-physical-cofactor-conditions.md)
的同一个 $h=k$ 原值图，本次加入两个 singleton 的全部原 $N/P$ 值条件。
完整得到四条新的物理必要多项式
$$
F_{N,e}=F_{N,o}=F_{P,e}=F_{P,o}=0.
$$
它们对 $(\lambda,u,Q)$ 的次数依次为
$$
(74,19,9),\quad(70,18,8),\quad(85,21,10),\quad(79,20,10).
$$
每一条都由同一点原行和完整四列多项式身份给出。整个 $NV$ 斜率零面、
$\Delta=0$ 及其它未付头零面都保留。这里没有排空原图、没有有限点数结论。

本次原定义用真正 dual 乘法；旧 compact 的错误均值、旧覆盖和其派生单位
没有进入输入。已成的五行 cofactor 与三因式分解均未重跑。

## 2. 同一点的完整原恢复

保留原记号
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,\quad\ell=A^3/B^2,\quad T=A^2/B,
$$
$$
h=k=1+\xi,\quad w=\lambda-1-T,\quad \delta=1-Q,\quad m=u-\ell,
\quad M=\ell(2u-\ell Q)-u^2=4bc\delta.
$$
本次声明坐标图仅为 $ABQ\delta P_f\ne0$；实际物理条件保 $bcP_{02}\ne0$。
原 $E_0,N_0,P_1$ 恢复的 $f,v_n,W_*,NV$ 使用前篇的确定性参数定义。
设
$$
V=v_n/Q,\quad W=W_*/2,\quad t=z/Q,\qquad
x=\frac{(u-\ell Q)V-mW}{M},\quad
y=\frac{\ell W-uV}{M}.
$$
在完整二次代数 $\rho^2=\delta$ 上，取
$$
p=1+\rho,\quad q=1-\rho,\quad
b=\ell/2+\rho m/(2\delta),\quad c=\ell/2-\rho m/(2\delta),
$$
$$
X=x+\rho y,\quad Y=x-\rho y,\quad
r=X-(1-\ell)p-ct,\quad s=Y-(1-\ell)q-bt,
\quad A_1=2f-2V+2bc\,t.
$$
由四行
$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,t),\quad g_C=(q,s,t,0)
$$
直接定义 $DK,\tau,N_4,P_2$，乘法的一阶项始终是
$(ab)_1=a_0b_1+a_1b_0$。

实际完整返回
$$
bX+cY=V,\quad bpX+cqY=W,\quad E_0=0,\quad
P_2(g_0)=P_{02},\quad N_4(g_0)=2\lambda P_{02},
$$
$$
P_j=3wP_{02},\qquad
\tau(\mathcal V)=\lambda,\quad
\tau(\mathcal V^2)=2\lambda^2,\quad
\tau(\mathcal V^3)=4\lambda^3,\quad
QN_4(\mathcal V)=2NV,
$$
其中 $\mathcal V=(1,w,h,h)$。没有把不同投影根的几何坐标拼接。

## 3. 四个真正原三次式

取
$$
E_{N,B}=N_4(g_B)-2\lambda P_{02}h^2,\qquad
E_{N,C}=N_4(g_C)-2\lambda P_{02}h^2,
$$
$$
E_{P,B}=P_2(g_B)-P_{02}h^3,\qquad
E_{P,C}=P_2(g_C)-P_{02}h^3.
$$
两个 C 行均已完整返回为 B 行的 $\rho$ 共轭。因此同时满足两个原值条件、
且 $\rho\ne0$，必使偶、奇部分分别为零。保留四条
$$
NBe,\quad NBo,\quad PBe,\quad PBo.
$$
实际每条对 $z$ 都恰为三次。没有从单个选定 $\rho$ 根的一个零式
误推出全部系数为零。

每行先取完整有理分母的最小公倍数，再只移去已付的共同物理内容，
最后按源中明确的首项有理常数规范化。所有四个系数均逐项还原到原有理式。
同样清 $NV$ 为同一原点的一次式
$$
NV_{\rm clear}=b_0+a_0z.
$$
其常数列次数为 $(24,5,4)$、375 项；斜率列为 $(24,6,3)$、318 项。
本次不将 $a_0$ 当单位。

允许清除的因子仅为
$$
A,\ B,\ Q,\ \delta,\ P_f,\ M,\ P_{02},\ \lambda,\ 2\lambda-1.
$$
$\lambda\ne0$ 来自已完成的原非零孤立 mean 规范；
$2\lambda-1\ne0$ 来自独立 347c 的完整原五列物理秩排除，
详前篇 §5。后一个不是裸均值理想的单位，不能去掉它的物理前提。
未付的 $\Phi,\Delta$ 及其它权因子没有被除去。

## 4. 包含所有斜率零纤维的四列恒等式

对任一个清式 $P(z)=\sum_{j=0}^3P_jz^j$ 定义
$$
R_P=\sum_{j=0}^3P_j(-b_0)^j a_0^{3-j}.
$$
本次实际逐项乘回
$$
\boxed{
a_0^3P(z)-R_P=(b_0+a_0z)H_P(z),
}
$$
其中明确的原乘子为
$$
H_P(z)=\sum_{j=1}^3P_j\sum_{k=0}^{j-1}
a_0^{2-k}(-b_0)^kz^{j-1-k}.
$$
这是全部四个 $z$ 系数的多项式身份，包括 $a_0=0$。
故原点必令 $R_P=0$；不能把它误解成只在
$z=-b_0/a_0$ 的有理代入图上成立。

对四个 $R_P$，源再只除已付物理内容并首项规范化，得到第一节四个 $F$。
实际删除的支持均来自 $Q,\delta,P_f,M,2\lambda-1$，
两个 N 行还用到了 B 的因子；删除的每个商积都完整回乘。
精确参数定义与规范 SHA 为：

| 原行 | 次数 $(\lambda,u,Q)$ | 总次数 | 项数 | 规范必要核 SHA256 |
|---|---:|---:|---:|---|
| NBe | (74,19,9) | 93 | 7065 | ac6cc4d42183ca23e5b74e2755966680ea2c240564e3401fbe2d4c3b7b75efe8 |
| NBo | (70,18,8) | 88 | 5907 | 084daba973f0b2f4a65ae849d19a9be72e86d5ac93943a808924b077e22542ed |
| PBe | (85,21,10) | 106 | 9482 | 3fbd20c0e8798015e4c4664c5ab962c1fb005c2c02d00692f4a4e0a7a60fff59 |
| PBo | (79,20,10) | 99 | 7927 | 5f68ed5598e1da2dcb63258bf54110bd32589bad7672db892fc159101819aeb2 |

规范序列是源中的升序单项指数三元组及精确有理系数序列。
每一核的完整 QQ 因式分解都只含一个非常数不可约因子，重数一；
非零有理内容和完整因式乘回均在回执。分解不改变必要性，也不支付新单位。

## 5. 唯一实际执行与开放范围

[冻结源](../notes/2026-11-28-unit211-h-equals-k-corrected-individual-NP-NV-scalar-returns-8542.py)
为 10461 字节；Git blob bb534b16c2858c7cec98c5358ca105758e736e67，
SHA256 00d513d603f862ef6b484176fe4d9da3b766e0047d46a87ec8f575622aa8ca14。

它只再生 f33 的 4540 字节成功坐标前缀，SHA256
a56e54b840cc323675394f96484c99658cad9a8420933cd2f344fe2df0d76efc；
旧五行/cofactor/因式尾均不执行。原预算 180 秒 / 4 GiB，没有延长。

- run 46109871971，job 140870807802。
- source commit 7b9c9becb081552a8c55fd4d52f862eb804d713a。
- 实际 pull 于 04:57:29.729980 UTC 到 111f36cc51dd4471dea25782e8dc013580b59866，两 README 无变。
- 实际 20.773897299 秒，峰值 191932 KiB，内层 exit 0。
- 四个完整原三次式、四条全部列恒等式、354 次精确除法均完整返回。
- stdout 10553 字节，SHA256 339342796274645455540cde2ed15824905bdea1eac8ffc973f05e6d7483b706。

[小回执](../notes/2026-11-28-unit211-h-equals-k-corrected-individual-NP-NV-scalar-returns-execution-8542.json)
只保定义、次数、SHA 与实际状态，不保可重算大系数载荷。
下一输入可使用这四个已完成的必要定义；不能把原共同零点、$\Delta=0$
或其它未付图默认为空。普通 Hilbert ISP 尚未完成。
