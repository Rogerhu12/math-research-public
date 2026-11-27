# R150：一般等权图的整个 singleton 均值 y=1 分支为空

**状态：已证明。** 在原 unit $2+1+1$ 非零孤立均值图中，规范 $p+q=2$，若两个 singleton 权相等 $b=c$，则同一原均值的奇部坐标 $y$ 不可能等于1。本文不要求 $Q=1-u$、$\Delta=0$ 或 $W=0$。一般等权图仍开放；普通复 Hilbert ISP 未完成。

日期：2026-11-27（台北）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 原输入、单位与第一条强制身份

仍在已登记原 U-value atlas 中工作。写
$$
p=1+r,\quad q=1-r,\quad r^2=d=1-Q,\qquad
b=c=m/2,\quad \ell=u=m,\quad a=1-m.
$$
原已付条件包含
$$
m(m-1)Q(1-Q)P\ne0,\qquad
P=P_{02}=m(m-1)(2m+3Q-4).
\tag{1}
$$
其中 $P=2P_0$。没有将一般等权条件当成可自由缩放的选择。

原 Frobenius 代数、Gram、均值及 $N_4,P_2$ 的完整定义沿用
[原均值边界证明的第1—2节](R150-appendix-unit211-Q1minusU-singleton-mean-y1-exclusion.md)；
那些定义本身在代入其 $Q=1-u$ 特殊条件之前成立。具体仍为
$$
\tau(v)=a v_0+v_1+bv_B+cv_C,
$$
乘法为双数块加两个 singleton 块，原 Gram 的行是
$$
k_0=(0,0,p,q),\quad
k_1=(0,A_G,r_G,s_G),\quad
k_B=(p,r_G,0,t),\quad k_C=(q,s_G,t,0).
$$
令
$$
X=x+yr,\quad Y=x-yr,\quad
f=\frac{x+dy}{2}-\frac{1+d-2m}{4},
$$
$$
r_G=X-ap-ct,\quad s_G=Y-aq-bt,\quad
A_G=2f-2bX-2cY+2bct.
\tag{2}
$$
它们是同一原均值和同一原 $f,t$，不是独立的影子变量。

从原 singleton 均值 $E_B=E_{Be}+E_{Bo}r$ 直接展开 (2) 得
$$
E_{Bo}=2dy^2+(-2x+1-3d)y+
 2mx+d-1+2m-2m^2+mt(y-1).
\tag{3}
$$
因此在 $y=1$ 上
$$
E_{Bo}=2(m-1)(x-m).
$$
由 (1)，原解必有 $x=m$。这是完整分支强制；没有倒置 $x-m$。

## 2. 原 E1 唯一恢复 t，保留全部 Q 纤维

以下代入 $x=m,y=1$，于是
$$
f=m-Q/4,\qquad
X=m+r,\quad Y=m-r.
$$
原双点均值及另一个 singleton 均值准确成为
$$
E_1=Q^2/2-2m+2m^2-m^2t,
$$
$$
2E_{Be}=m(t^2-2t)+4(1-Q)(m-1).
\tag{4}
$$
整个二次代数的奇部 $E_{Bo}$ 已恒零；另一 singleton 均值是其共轭。由原 $m\ne0$，(4) 第一式唯一给
$$
t=\frac{4m(m-1)+Q^2}{2m^2}.
\tag{5}
$$
把同一个 (5) 返回第二式并清除已付的 $m$ 幂，得到首一原必要四次式
$$
G(m,Q)=Q^4+4m(m-2)Q^2-16m^3(m-1)Q
       +16m^2(m-1)^2=0.
\tag{6}
$$
由于 $G$ 对 $Q$ 首一，以它作余式不除任何参数首项。

## 3. 另三条原必要式的确定构造

为完整指定算术输入，令 $\mathbf d=D_K1$，
$$
N_4(v)=2\tau(\mathbf d v^2)-2f\tau(v^2)
 -4\tau(v)\tau(\mathbf d v)+4f\tau(v)^2+\tau(vD_Kv),
$$
$$
P_2(v)=\tau((v-\tau(v)1)^3).
$$
定义同一个原 Gram 的多项式
$$
L=\tfrac12N_4(k_0),\qquad
J_0=\tau((k_0-\tau(k_0)1)^2(k_1-\tau(k_1)1)),
$$
$$
V=N_4(k_0+k_1)-N_4(k_0)-N_4(k_1),
$$
$$
N_B=bN_4(k_B)+cN_4(k_C),\qquad
P_B=bP_2(k_B)+cP_2(k_C).
\tag{7}
$$
这里 $J_0$ 不是权参数 $J$。原 $N_0/P_1$ 值身份给
$$
L=\lambda P,\qquad J_0=wP,\qquad T=\lambda-1-w.
$$
因此原双点 $N_H$ 及加权 singleton 的 $N_S,P_S$ 分别迫使
$$
F_N=PV-4LJ_0=0,
$$
$$
F_S=P^2N_B-2(m-1)LP^2+4LJ_0P-4L^3=0,
$$
$$
F_P=P^2P_B-(m-1)P^3+3J_0P^2-4L^3=0.
\tag{8}
$$
例如，原矩值中的
$$
m+2T+(2\lambda^2-2\lambda+1)=m-1-2w+2\lambda^2,
$$
$$
m+3T+3(2\lambda^2-2\lambda+1)
 +(4\lambda^3-6\lambda^2+3\lambda-1)
 =m-1-3w+4\lambda^3
$$
正给 (8) 后两式；不把这三个加权必要条件声称为全部原方程的充分条件。

以下清分母规则唯一确定使用的三个多项式。若 $F$ 的 $t$ 次数是 $s$，将 (5) 代入后乘以 $(2m^2)^s$，再以首一的 $G$ 对 $Q$ 取余。对 $F_N,F_S,F_P$，实际 $s=2,3,3$。所得余式的全部 $\mathbb Q[m]$ 系数共同内容准确为
$$
m^5,\qquad m^8,\qquad m^7
$$
（内容取首一）。仅除去这些已付单位，记所得三式为
$$
N(m,Q),\quad S(m,Q),\quad Z(m,Q).
\tag{9}
$$
它们的 $(\deg_m,\deg_Q)$ 分别为 $(6,3),(8,3),(9,3)$，项数为21、30、35。完整定义由 (2)、(7)—(9) 给出，不需要缓存文件、猜测因子或选数值嵌入。

供直接核对，$N=\sum_{j=0}^3n_j(m)Q^j$ 的系数为
$$
n_0=64m^6-320m^5+608m^4-480m^3+96m^2+32m,
$$
$$
n_1=-64m^6+256m^5-440m^4+232m^3+88m^2-72m,
$$
$$
n_2=32m^4-20m^3-24m^2+4m-8,\qquad
n_3=-12m^3+26m^2-20m+14.
\tag{10}
$$
附源从整个原 Gram 构建 (7)，没有把 (10) 作为替代输入。

## 4. 完整原结式的 14 次权覆盖

在 $\mathbb Q[m]$ 中，固定完整 $Q$ 次数4与3，取三个7阶 Sylvester 行列式
$$
C_N=\operatorname{Res}_Q(G,N),\quad
C_S=\operatorname{Res}_Q(G,S),\quad
C_Z=\operatorname{Res}_Q(G,Z).
\tag{11}
$$
它们的准确 $m$ 次数为26、37、41。每个原解必使三个完整行列式为零，包括任意 $Q$ 首项或中间消元主元为零的权纤维。

附源采用 $\mathbb Q[m]$ 的无分式消元；每次除法都核回“商乘除数加余数等于原被除式”，要求中间 Bareiss 除法余数为零。没有将模多变量理想的单位性提升为特征零结论。

实际完整 QQ Euclid 及后继组合给
$$
A(m)C_N+B(m)C_S
 =m^4(m-1)^7(m-\tfrac12)^3,
\tag{12}
$$
其中 $\deg A=22,\deg B=11$。该整条身份已实际乘回；三项形式的 $C_Z$ 系数准确为零。完整右端也逐因子乘回，次数14，不漏隐藏因子。组合系数可由附源再生，规范序列的 SHA-256 保于执行回执，不保存可重算的长系数表。

由 (1)、(11)—(12)，原解只能有
$$
m=\tfrac12.
\tag{13}
$$

## 5. 最后半权的两个原式已经矛盾

将同一个 $m=1/2$ 返回 (6)、(9)，得到
$$
G_{1/2}(Q)=Q^4-3Q^2+Q+1,
$$
$$
N_{1/2}(Q)=9Q^3-\tfrac{25}{2}Q^2-\tfrac{11}{2}Q+9.
$$
准确有理 Bézout 恒等式为
$$
\frac{-1225-2682Q}{757}G_{1/2}
+\frac{52+550Q+298Q^2}{757}N_{1/2}
=Q-1.
\tag{14}
$$
两个原必要式同时为零便迫使 $Q=1$，与 (1) 矛盾。无需再选择 $S,Z$ 的根，也没有把来自不同纤维的根拼合。

至此整个原等权 $y=1$ 支为空。它与已闭的 $Q=1-u,y=1$ 边界是不同的完整范围；一般等权图可合法在 $y\ne1$ 上继续，尚未证明该整图为空。

## 6. 实际执行源、身份与再生方式

两份文件保存**实际执行的函数体原字节**，均为纯 JavaScript BigInt 有理算术，无外部 CAS：

- [原 Gram、余式及完整 QQ 结式](../notes/2026-11-27-unit211-equal-weight-y1-original-QQ-return-8542.js)，SHA-256：0fdc1f60daf94f572a6dbe3d623b183bde3684da1c18425161a47c9074dd2157。
- [完整原结式组合及半权 Bézout](../notes/2026-11-27-unit211-equal-weight-y1-original-certificate-8542.js)，SHA-256：c9cc105deb5ce3f0583563aa32d3cd214acf9897dcd5cee3b276197c14ae51cd。
- [小执行回执](../notes/2026-11-27-unit211-equal-weight-y1-execution-8542.json)。

实际运行在 functions.exec 的 V8 中：首源内部原重建0.029秒、完整结式阶段29.274秒；后继完整组合和原半权返回39.034秒，调用正常完成。该执行方式没有暴露进程退出码或 RSS，回执不伪造这些字段。这里只保存源、参数和规范输出 SHA，不保存可再生的结式或长 Bézout 数组。

从课题目录在可用 Node 环境再生时，读取这两个函数体并按同一调用方式执行：
~~~js
const fs = require("fs");
const build = fs.readFileSync(
  "notes/2026-11-27-unit211-equal-weight-y1-original-QQ-return-8542.js", "utf8");
const certify = fs.readFileSync(
  "notes/2026-11-27-unit211-equal-weight-y1-original-certificate-8542.js", "utf8");
const built = new Function(build)();
const proof = new Function(certify)(built.report);
console.log({
  degrees: built.report.resultantDegrees,
  cover: proof.coverFactorization,
  excluded: proof.wholeEqualWeightYOneExcluded
});
~~~

这只是已成功阶段的再生方法，不把再跑一次设置为数学登记门槛。后续仍需一般等权图的 $y\ne1$ 原返回、其它 essential 分支和真正算子桥。
