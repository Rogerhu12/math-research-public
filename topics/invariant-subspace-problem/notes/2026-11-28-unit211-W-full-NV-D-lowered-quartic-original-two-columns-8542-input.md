# 新输入：完整原 N4(V) 的 D 降幂四次与两条原均值

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。
本源尚未执行；首次预算固定 180 秒、4 GiB。
源 SHA256：5b37354dc4794e4a8d0c7dbb4f2799fc10f39e4462eb5764c93a5638bc460f74；源长度 11488 字节。
建议源 basename：
2026-11-28-unit211-W-full-NV-D-lowered-quartic-original-two-columns-8542.py。

## 1. 原范围和这次真正新增的条件

范围仍是当前 W、原两个 singleton 值互异的图。原物理
$D=\ell A_\lambda-T^2=bc(h_U-k_U)^2\ne0$。
只使用此图已经支付的纯权单位；不外推到 $h_U=k_U$。

[两个原四次必要式](../results/R150-appendix-unit211-W-original-two-quartic-necessary-values.md)和
[原奇 N/P 与完整 N4(V) 的低 D 理想压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)
已给出
$$
C_4=2mD\,a_\Delta+K\,b_\Delta,\qquad
\ell^2V_{\rm low}
=D\widetilde Z_0+\frac K{2m}\widetilde Z_1
+\frac{D^2}{M}\widetilde Z_2. \tag{1}
$$
这里 $m=u-\ell$、$M=4bc(1-Q)$，均为当前图的已付单位；
$K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3$，
$A_\lambda=2\lambda^2-2\lambda+1$，
$B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1$。

定义真正的新四次
$$
B_4=b_\Delta\left(\widetilde Z_0+\frac D M\widetilde Z_2\right)
-a_\Delta\widetilde Z_1. \tag{2}
$$
在不倒置 $b_\Delta$ 的原环中直接有
$$
(2m\ell^2b_\Delta)V_{\rm low}
-\widetilde Z_1C_4=2mD B_4. \tag{3}
$$
因此每个当前原物理解必有 $B_4=0$。这是一次合法使用原物理
$D\ne0$ 的必要条件，不是从模零推回 QQ。整条 $b_\Delta=0$
仍保留；不宣称以 $B_4$ 取代 $V_{\rm low}$ 后得到等价系统。

证明 (3) 只需对三个形式变量
$(\widetilde Z_0,\widetilde Z_1,\widetilde Z_2)$ 比较系数：
$$
2m b_\Delta
\left(D,\frac K{2m},\frac{D^2}{M}\right)
-(0,C_4,0)
=2mD\left(b_\Delta,-a_\Delta,\frac{b_\Delta D}{M}\right).
\tag{4}
$$
新源会将 (4) 的三个完整系数乘积实际返回；没有再生旧
$V_{\rm low}$ 大多项式或其冻结换基尾。

## 2. 完整原值的短式定义

使用新独立一般引理
[三个缩放完整 N4 短式](../results/R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)。
该引理的九自由变量原 Gram 源为
2026-11-28-unit211-general-scaled-entire-N4-three-compact-identities-8542.js，
SHA256 为
39b490ebb38cb807dc5a1401d2156561698d0d213e42ac5e065770cb31c2bf29。
它已实际返回全部九个差式；本次只引用其完整原身份，不重跑。

记 $V=bX+cY$，$W_1=bpX+cqY$，$w=\lambda-1-T$，
$c_\lambda=3-2\lambda$，$A_1$ 为原 double-germ 的 Gram 对角。
则
$$
\begin{aligned}
\widetilde Z_0={}&\ell^2 A_1+4\ell^2(1-2\lambda)f+2\ell fD\\
&+2\ell u w(\ell c_\lambda+T)
+2V(\ell^2+\ell c_\lambda T+T^2)
+2bc\,t(T^2-\ell^2),\\
\widetilde Z_1={}&2(\ell c_\lambda+2T)(uV-\ell W_1)
-2\ell M w+4bc\,mTt,\\
\widetilde Z_2={}&2\{(u^2-\ell^2Q)V-2m\ell W_1-\ell Mf-bcMt\}.
\end{aligned}\tag{5}
$$
这些是完整 $N_4$ 与完整极化，不是某个分量，也没有以 $\Phi$
倍数代替原 $N_4$。其原一般证明未倒 $\ell$；本次仍限上述当前 W 图。

把
$$
A_*=4uQ-J,\qquad C_*=A_*m^2+J(1-Q)\ell^2
$$
代入，原两系数是
$$
\begin{aligned}
a_\Delta={}&M\ell^2Q(3-4\lambda)+MA_*T^2
+2MuQ c_\lambda\ell T+DC_*,\\
b_\Delta={}&2Mm(A_*T+uQ c_\lambda\ell).
\end{aligned}\tag{6}
$$
在旧 native 坐标 $(x,y,t)$ 中，$\lambda,T,f,V,W_1,A_1$
皆仿射，(5) 三式几何次数分别至多 $3,2,1$，
$a_\Delta,b_\Delta$ 次数至多 $2,1$。
所以 (2) 的几何次数至多 $4$。源会核完整原分子此次数；
若不成立就失败保留，不能删断言。

这改变了原输入：旧完整 $V_{\rm low}$ 包含 $K\widetilde Z_1$、
$D^2\widetilde Z_2$ 的五次项；本次用原 $C_4$ 真组合得到四次，
没有重启旧五次值的换基、旧十二次乘法动作或旧余子式。

## 3. 一次新的 native 原四次返回

只从两份固定依赖读取必要定义：

1. 2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py，
   全源 SHA256
   18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b。
   截到 newfive=rawthree[:] 前 9855 字节，
   前缀 SHA256
   c1436ea6bb67d4c720016091fb65f439be5bfcc7af131c00a0749321fcf45e43。
   只构造原坐标、三均值和全图首一 $q_\alpha$；
   不执行旧十行、旧三个标量。
2. 2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py，
   全源 SHA256
   10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1。
   必要前缀 14656 字节，SHA256
   88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8。
   不执行其旧乘法矩阵或 parameter cofactor 尾。

只对新 $B_4$ 调用一次完整 native 归约器，得到
$$
\mathbf r\mathbf b-B_4=\sum_{j=0}^3\tau_j F_j,\qquad
\mathbf b=(1,x,y,t,y^2,yt)^t. \tag{7}
$$
右边仅原四条均值；对 NS/PS 的两个来源坐标必须为零。
归约器自己的旧分母白名单保持原字节，不放宽。
只有实际 (7) 成功才登记原四次六列接口。

## 4. 六个基元一次短除与多项式收缩

[全 alpha/chi 十行原图](../results/R150-appendix-unit211-W-alpha-chi-exact-original-ten-by-two-and-three-scalars.md)
已给出纯权分母的可逆原坐标以及
$$
q_\alpha=\alpha^2+q_1(e,k,\chi)\alpha+q_0(e,k,\chi)
\in I_4. \tag{8}
$$
其全部权分母都已付；不倒任何 $\chi$ 首项。

每个 $b_i$ 在 $\alpha$ 上次数至多二。对这六个基元各短除一次，
选一个共同纯权单位 $D_B$ 后得
$$
D_B b_i=B_{i0}+B_{i1}\alpha+H_iq_\alpha. \tag{9}
$$
源以共同 $Q_\alpha$ 清 $q_0,q_1$ 的权分母，逐项返回十二个
非平凡系数乘积；$\alpha^2$ 的六个坐标由首一性直接对应。
这不是将六生成元假设为自由。

对 (7) 的六个实际系数另取共同纯权单位 $D_R$，
令 $r_i'=D_Rr_i$。只作多项式线性收缩
$$
B_j'=\sum_i r_i'B_{ij},\qquad H'=\sum_i r_i'H_i.
$$
逐个收缩 (9) 的完整乘回后，与 (7) 合成
$$
D_BD_R B_4
=B_0'+B_1'\alpha+H'q_\alpha
-D_BD_R\sum_j\tau_jF_j. \tag{10}
$$
所有实际收缩系数、来源 DAG 与清分母身份保持同一点；
不另把巨大有理式统一分母再展开一次作为额外门。
日志明确区分「六个完整基元身份的实际线性组合」与
未执行的巨大有理式重新展开。

只剥两列公共内容中已经支付的纯权因子，得到新必要两列。
任何未付 $\chi$ 内容或 $b_\Delta$ 因子均保留，不作逆。

## 5. 两个真正新的小目标及其零面

只取新 $B_4$ 行分别与原 $E_W$、原 $E_{Bo}$ 的两个固定 pair。
原 N1、NS、PS 及全部个别原值继续保留；这两个新标量仅是必要式。

若两行是 $(r_0,r_1)$、$(s_0,s_1)$，先取
$g=\gcd(s_1,-r_1)$。仅将两个实际乘子共同精除，得
$$
\mu=s_1/g,\quad \nu=-r_1/g,\quad
C=\mu r_0+\nu s_0,\quad \mu r_1+\nu s_1=0. \tag{11}
$$
源必须返回完整两列乘积。这是新的原组合，
所以 $g=0$ 整纤维也被 (11) 覆盖，未把原方程除以未付因子。
若两个 $\alpha$ 系数均零，则原常数行完整保留，不调用除零。

最终仍只剥已付纯权单位。没有固定预期的非零投影或排空；
任一实际资源/实现边界如实记录最后完整阶段，未返回对象不写成功。

## 6. 运行边界和归档

两层前缀的 alarm/setitimer 都钳到原 180 秒绝对截止；
RLIMIT_AS 为 4 GiB，依赖前缀没有降低此硬界。
只保存源、小参数定义、真实运行 ID、次数/项数/字节数/SHA 与小回执。
不输出或存储大系数、矩阵、encoded payload、分片缓存。
旧 17703 的白名单失败、2d722 的完整值换基超时均保持原身份，
本源不重启它们。
