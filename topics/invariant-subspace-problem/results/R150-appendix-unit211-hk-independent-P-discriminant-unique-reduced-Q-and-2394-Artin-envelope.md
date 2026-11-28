# R150：独立 P 判别式、碰撞 Delta 零的唯一约化 Q 与 2394 维比值包络

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

**状态：完整证明；新判别式唯一首次实际成功。** 当前正确 $h=k,\Delta=0$ 原图中，已有约化基 $K_{99}\times K_{300}$ 上的原 $u$ 唯一。新的独立 $P$ 判别式在这两个谱域均为单位；结合原固定四阶 $Q$ 结式的一阶赋值，原 $\Delta,T_{\rm num}$ 的共同 $Q$ 也唯一且约化。

因此，在原已付权支持的准确局部化后，$(\lambda,u,Q)$ 的必要权代数是 $K_{99}\times K_{300}$ 的某些整分量，QQ 维数至多 $399$。原倒 $z$ 三次与 $\rho$ 二次给明确比值/Gram 坐标的 Artin 包络
$$
\boxed{\dim_{\mathbb Q}\mathcal E_{\rm new}\le399\cdot3\cdot2=2394.}
\tag{1}
$$
另添独立原尺度 $U_0^3=-P_0$ 后，包络长度至多 $7182$。本条不证明两个谱域排空，不处理 $\Delta\ne0$，不计未列物理矩阵轨道，普通 Hilbert ISP 仍未完成。

## 1. 已成约化 u 基与独立原 P

[约化权基与前一个4788包络](R150-appendix-unit211-hk-Delta-zero-reduced-base-and-4788-coordinate-Artin-envelope.md)已经证明
$$
\mathcal A_0=
\mathbb Q[\lambda,\Sigma^{-1},u]/(P,M_{\rm true})
\simeq K_{99}\times K_{300},\qquad
K_d=\mathbb Q[\lambda]/(F_d).
\tag{2}
$$
$F_{99},F_{300}$ 是不同的 QQ 不可约谱多项式，在原固定十七阶行列式中均重数一。每个 $K_d$ 分量中
$$
u=\eta_d\in K_d.
\tag{3}
$$
这是已完成的整域结构结论，不提供 $\eta_d$ 的显式系数。冻结 ad00 的联合 gcd 实际仍未返回，本篇没有恢复或重跑它。

独立正确 $P$ 来自原 $\Delta,T_{\rm num}$ 的 $Q$ 结式，与错误 compact mean 无关。它的已成准确参数是
$$
\deg_{\lambda,u}P=(28,3),\qquad \#\operatorname{supp}P=115.
$$
规范 JSON 为 2496 字节，SHA256
8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c。

本次只在 runner 临时目录读这个参数，按 SHA 唯一选择；同一旧历史中的错误均值投影不读取、不执行、不导入。正确原来源及隔离边界沿[更正后的722覆盖](R150-appendix-unit211-h-equals-k-corrected-Delta-zero-722-base-cover.md)和[固定十七阶覆盖](R150-appendix-unit211-h-equals-k-corrected-fixed-seventeen-lambda-cover-and-5640-points.md)。

## 2. 新三次判别式的完整实际返回

按原 $u$ 写
$$
P=a(\lambda)u^3+b(\lambda)u^2+c(\lambda)u+d(\lambda).
\tag{4}
$$
本次先将四系数全项重拼为原115项，返回完全相等。真实系数次数按 $(d,c,b,a)$ 顺序为 $(27,28,28,28)$，且 $a\ne0$。

新计算是标准三次判别式
$$
\mathscr D(\lambda)=
18abcd-4b^3d+b^2c^2-4ac^3-27a^2d^2.
\tag{5}
$$
实际 $\deg\mathscr D=112$、112个非零项，规范字节数5377，SHA256
ab1807e14cee700b778c64a146c202f5c1617f7863f3675c97754bc014e61326。

完整 QQ 因式分解的实际记录如下。每一行表示一个 QQ 不可约因子，重复次数完整保留：

| 次数 | 重数 | 规范因子 SHA256 |
|---:|---:|---|
| 1 | 1 | 53d7f4a048bd0daee134c84d46a9de1de3d4c71942f740eb4f964d3fccbeecf3 |
| 31 | 1 | 5085e6531c3565baebd8cb653576daecd56c9d7ba88687b4f81fba53cde1287c |
| 1 | 2 | 1e532a5952d159b9db2f494f1ccb8115c6a4076818c2aedead7150da17f15982 |
| 19 | 2 | 0c9c681adccc960a7e9f6c097b7e8bf3576827d64d45cf9cb64029a8d0b4b235 |
| 1 | 4 | 1fa1f30d60b5195a920cd9a68370231ccdd314c1cf5245eb80f5bb78541a427e |
| 2 | 4 | 76c6537baea2267477ffc856f1865cc27d5c76cab43f750c63a88cbbdccbf3ab |
| 2 | 14 | 5e8ee6f750b38f2c3698e1aefc7ced1482ccb207059d152c37393a670eb1dc81 |

常数是 $1/12116574790945106558976$，全部因子带重数乘回 (5) 成功。加权次数
$$
1+31+2+38+4+8+28=112.
$$
最高不可约次数为31，小于99。因此 $\mathscr D$ 在两个 $K_d$ 中均非零，也就是单位。又因 $a$ 的次数28小于99，$P_d$ 在两个整域上均是准确三次、判别式非零，故
$$
P_d\in K_d[u]\ \text{可分}.
\tag{6}
$$
这里没有选择一个复嵌入或有限素数；也没有从 QQ 不可约误推复绝对不可约。

由 (3)、(6)，在 $u=\eta_d$ 处准确有
$$
\operatorname{ord}_{u-\eta_d}P_d=1.
\tag{7}
$$

## 3. 原四阶 Q 结式与旧剥除乘子

这一步保留原式的来源，不能只由裸 $P$ 的简单根直接声称同一个 $Q$ 唯一。

设 $D_0(\lambda,u,Q)$ 与 $N_0(\lambda,u,Q)$ 是独立 $P$ 原执行中使用的两个准确 primitive 多项式。它们来自原 $\Delta,T_{\rm num}$，准确记录如下：

- $D_0$：双权与Q次数 $(12,4,2)$、98项，SHA256
  6e482757458656b38ee447c7509286fe03dd15fb93d1e45e84fbbeaac0ed66ef；
- $N_0$：次数 $(19,5,2)$、180项，SHA256
  e3e679e52d776c3805e31681c2040d5a04b8ad99ac61a5933444e9a7f9576085。

$\Delta$ 的分母只由原 $A,B$ 支持组成，primitive 操作没有剥除其任何非恒定分子因子。$T_{\rm num}$ 的 primitive 操作只剥原已付 $Q$ 和 $S$ 支持，并保准确乘回。因此在原 $Q$ 单位图上，$(D_0,N_0)$ 与原 $(\Delta,T_{\rm num})$ 等价。

原固定四阶 Sylvester 结式为
$$
R_4(\lambda,u)=\operatorname{Res}_Q(D_0,N_0).
\tag{8}
$$
实际原 $Q$ 次数固定为二、二；$R_4$ 的双次数为 $(55,10)$，SHA256
e5830d2fd122f621b1f5b94f6cf87096c8060669883e4ad95fcd1322d9a49d93。

其旧准确剥除记录只包含
$$
A,\ B,\ u,\ u-1,\ S
\tag{9}
$$
的原已付支持，且全部正反乘回。故
$$
R_4=U(\lambda,u)P,\qquad
U\ \text{仅由(9)的支持及非零常数组成}.
\tag{10}
$$
这不要求某个 Q 首项可逆，也没有剥除未知权因子。

现在先对 (2) 加入原 $u(u-1)$ 局部化。因为 (2) 是两个域的乘积，局部化只会删去某些整分量。对任一保留的 $K_d$，$\eta_d(\eta_d-1)\ne0$。原 $A,B,S$ 也在该域中为单位；它们的支持是次数小于99的非零谱多项式。

因此在离散赋值环
$$
\mathcal O_d=K_d[u]_{(u-\eta_d)}
\tag{11}
$$
中，(10) 的 $U$ 是单位。结合 (7)，准确得到
$$
\operatorname{ord}_{u-\eta_d}R_4=1.
\tag{12}
$$
如果某个整分量已经被原 $u(u-1)$ 局部化删除，它本来就没有原物理点，不需要对它作 (11)。

## 4. 固定四阶原矩阵的一阶赋值给同 Q 唯一约化

原 $\Delta$ 的 Q 二次系数由已刊完整原展开给出：
$$
[Q^2]\Delta
=-\frac{2(B^2-A^3)(\lambda^2+\lambda-1)}{B^2}.
\tag{13}
$$
分子是非零谱多项式，次数至多八。由于 $D_0$ 没有剥非恒定分子因子，它的 Q 二次头也仅差一个原 $A,B$ 单位。所以 $D_0$ 在 $\mathcal O_d[Q]$ 及其剩余域 $K_d[Q]$ 中都准确为二次，且头为单位。

把 (8) 的完整四阶 Sylvester 矩阵看作 $\mathcal O_d$ 上的矩阵。由 (12)，其 Smith 对角中恰有一个非单位项，赋值一；其余三个项为单位。因此模 $u-\eta_d$ 后，矩阵的核维为一。

令 $D_d,N_d\in K_d[Q]$ 是同点特化。设
$$
g_d=\gcd(D_d,N_d),\qquad r_d=\deg g_d.
$$
固定四阶 Sylvester 映射的核为
$$
A(Q)D_d+B(Q)N_d=0,\qquad \deg A,\deg B<2.
$$
写 $D_d=g_dd_1$、$N_d=g_dn_1$，所有核元素为
$$
A=-n_1H,\qquad B=d_1H,\qquad \deg H<r_d.
\tag{14}
$$
后一限制来自 $\deg D_d=2$；它也自动保证 $\deg A<2$，即使 $N_d$ 的 Q 次数下降。若 $N_d=0$，核维等于二，同样符合这个公式。因此这一步不要求 $N_d$ 的 Q 首项为单位，也不遗漏它降次的整纤维。

核维一强制 $r_d=1$。故存在 $\theta_d\in K_d$ 使
$$
g_d=Q-\theta_d,\qquad
\boxed{K_d[Q]/(D_d,N_d)\simeq K_d.}
\tag{15}
$$
这证明共同 $Q$ 唯一，而且没有重数；它不只是至多一个不同 Q 的点集界。

在 (15) 中继续反演原 $Q,1-Q,bc,P_{02},P_f$ 等已经支付的原权支持，只会删去整域分量。$bc$ 可以在 $1-Q$ 已逆后由 $M/(4(1-Q))$ 定义。由第3节，原 $\Delta,T_{\rm num}$ 与 primitive 两式在这个准确开图等价。因此其必要权代数 $\mathcal B_{\rm new}$ 满足
$$
\mathcal B_{\rm new}\ \text{是 }K_{99}\times K_{300}\text{ 的整分量之积},
\qquad \dim_{\mathbb Q}\mathcal B_{\rm new}\le399.
\tag{16}
$$
还可加入其它原权单位或纯权关系；对域乘积的局部化及商仍只删整分量。

本证明没有计算 $\eta_d,\theta_d$ 的显式系数，也没有声称原八个 z 方程已经返回。同 Q 的原理想结论是由实际新判别式、原四阶结式恒等式和新的完整 Smith 论证共同得到的。

## 5. 2394 包络与独立尺度

在 (16) 上，沿[完整 Loww 纤维](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Loww-fibers-8664-cover.md)及[前一个Artin包络](R150-appendix-unit211-hk-Delta-zero-reduced-base-and-4788-coordinate-Artin-envelope.md)，
$$
L_w(z)=c_0+c_1z+c_2z^2+c_3z^3,\qquad
c_0=-2P_{02}\lambda^2(2\lambda-1)^2/B
$$
的 $c_0$ 是准确原单位，$z$ 也由完整原零值排除支付。令 $\zeta=z^{-1}$，得到首一三次
$$
\zeta^3+(c_1/c_0)\zeta^2+(c_2/c_0)\zeta+c_3/c_0=0.
\tag{17}
$$
先添这个首一三次，长度至多 $1197$，再作 $\zeta$ 的 Artin 局部化。然后添原首一二次
$$
\rho^2=1-Q.
\tag{18}
$$
得到 (1)。$z$ 的可能重数完整保留；(15) 的约化性并没有自动传成整个几何商约化。

其它已列原 Gram 与比值坐标按原 $P_f,Q,M$ 等单位唯一恢复。继续加入完整原值及非退化限制，只形成这个有限 Artin 包络的商和局部化，不增加长度。本条没有引入只适用于别的 W 分支的物理 D 单位。

明确计数范围仍为 $(\lambda,u,Q,z,\rho)$ 和由其唯一恢复的比值/Gram 坐标。原独立尺度必须另加
$$
U_0^3=-P_0.
$$
该式首一三次，给包括这一独立尺度的包络长度至多 $3\cdot2394=7182$。这仍不等于未列出的物理矩阵轨道数。

## 6. 唯一新实际执行与可再生凭据

源：[独立 P 的三次 u 判别式](../notes/2026-11-28-unit211-hk-independent-P-cubic-u-discriminant-8542.py)。
[首次输入说明](../notes/2026-11-28-unit211-hk-independent-P-cubic-u-discriminant-8542-input.md)；
[小实际回执](../notes/2026-11-28-unit211-hk-independent-P-cubic-u-discriminant-8542-execution.json)。

- 源 blob：164e42bad2d09a5738f5f18cdc59f2414ec80d92，3716字节；
- 源 SHA256：70b3cea6a303f2105e2cc448498d60387319389b6f04d8587adf6819cdea14f4；
- 唯一 run46148191389 / job140988760078；
- 源提交7f594b9ccd82a222446622f44bf55ad41330520c；
- 执行前真 pull6545eba205aceeee824a2eefffc627f8174e066f，2026-11-28T13:09:42.960604+00:00，两份README无变化；
- 初始60秒、1 GiB，外75秒；driver实际0.053066027秒，最大RSS40312 KiB，exit0；
- 数学0.002863149秒，数学进程RSS36544 KiB；
- stdout2855字节，SHA256 ada1e71665c9cf7464aa426f73feeaa059984aaee10f1a3fb087ada1b233fad1。

全部115项重拼、新判别式及完整QQ因式乘回在这唯一实际运行中完成。没有执行旧 P 投影、旧因式、M 或 F99/F300 再生、冻结联合 u-gcd、同 Q-gcd 或八原 z 门；没有保存可重算系数载荷。

此前首次发布已推送但因工作流文件名大小写不符而未派发，随后只改成既有全小写命名并成功派发本次唯一数学运行。准确发布边界另记[小记录](../notes/2026-11-28-root-publication-1845-dispatch-boundary-8542.json)，不把未执行的派发记为数学失败或重跑。

## 7. 未完成的原接口

两个谱域上的完整原 z 条件仍可能进一步删除整个分量，本条没有检查或宣称它们非空。Delta 非零图仍保，完整原碰撞及其它 rank 图继续。2394和7182是指定坐标包络的上界，不是普通 Hilbert 不变子空间问题的完成证书。
