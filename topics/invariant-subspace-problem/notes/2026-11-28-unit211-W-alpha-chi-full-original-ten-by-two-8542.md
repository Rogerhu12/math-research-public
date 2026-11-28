# 新输入：纯权分母 $\alpha,\chi$ 图中的完整原 I6 十行两列

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。源尚未执行，不预记新系数或原标量。

## 1. 与旧门的数学差别

使用[新的原 alpha/chi 多项式坐标](../results/R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md)，其分母只含当前 W 已付权。这里 $\chi=2\delta A_1/t-Z$ 是新标量，不是 singleton 值，也不是旧斜率 $s=t/(f-u)$。

本源不再构造旧 gamma 图，不读其原五式前缀，不重新运行此前九二次、native gamma 五二次或它们的任何标量。只取旧 native 六均值规则的 14656 字节定义前缀。新的目标是本多项式图的实际首一 $\alpha^2$、完整原 $I_6$ 十行两列，以及三个固定新两行原标量。

此前冻结的 $f$ 首一后十行展开依赖不同的 gamma 有理输入及原 cubic；这里全部系数分母为纯权单位、两原 native 余式已经对 $\alpha$ 二次。没有延时、换顺序或恢复旧未完成尾。

## 2. 正确原图

保持原 W 权及当前 $D\ne0$ distinct-singleton 范围。令
$$
m=u-\ell,\quad \delta=1-Q,\quad
\widehat U=u-\ell Q,\quad
M=\ell(2u-\ell Q)-u^2,\quad T_0=2u-\ell Q-2u^2,
$$
$$
Z=u(u-1)+\ell(1-\ell)Q,\quad
C=u-1+(1-\ell)Q,\quad
R_w=2u(1-u)-uQ+(2u-1)\ell Q.
$$
只用已证明的纯权单位 $m$、$R_w=-ue^2H_{\rm old}/\overline V$、$\delta$、$M$。原恢复为
$$
t=-\alpha\chi/(mR_w)-2\delta\ell/m,\quad
f=u+(\alpha+\widehat Ut)/(4\delta),
$$
$$
V=f+(M-Z-\chi)t/(4\delta),\quad
A_1=(\chi+Z)t/(2\delta),
$$
$$
W_1=(T_0+4uf)/2,\quad
x=(\widehat UV-mW_1)/M,\quad
y=(\ell W_1-uV)/M.
\tag{1}
$$
源完整返回正确 $\mathcal R=0$、$A_1$、$\alpha$、$\chi$ 和原两个加权线性恢复。$\alpha=0$ 没有被除；逆图只需要已付 $t$。原 $\lambda,T$ 仍由同一个 $E_0/N_0/P_1$ 图恢复。

## 3. 新实际首一二次

native 原四二次是
$$
E_1,E_B^{even},E_B^{odd},N_1.
$$
定义原线性部
$$
L_\alpha=(2\delta/u)(ux+\widehat Uy)-\widehat Ut.
$$
只对这个新 $L_\alpha^3$ 使用 native 六均值规则，实际返回
$$
L_\alpha^3-R_{\le2}=\sum_{i=0}^3H_iE_i.
$$
各 $H_i$ 总几何次数至多一。令 $d(\chi)$ 是 (1) 的 $\alpha$ 一次方向，源实际检查 $L_\alpha(d)=1$。取上式三次最高部并代入 $d$，再用 $\mathcal R=0$ 上
$$
E_1=EW,\qquad E_B^{even}=(EW-mE_B^{odd})/\ell,
$$
得到三原二次头的实际 Bézout $1$。该纸面存在性已刊；本次只是为真正新的完整二列输入构造它的系数，不能把显示这些系数设为旧定理成立的附加门。

记三个实际组合系数为 $c_j(\chi)$、$Q=(EW,E_B^{odd},N_1)$，则
$$
q_\alpha=\sum_{j=0}^2c_jQ_j
=\alpha^2+q_1(\chi)\alpha+q_0(\chi).
\tag{2}
$$
源逐项返回头恰为一、完整原组合和所有系数分母只由既有纯权单位组成。没有选单个 $\alpha$ 头作逆，也没有任何 $\chi$ 分母。

## 4. 完整原五二次到十行两列

两个 native NS/PS 余式在 $(1,x,y,t,y^2,yt)$ 上，分别是原三次系数一加原四二次的组合。源重新生成这两个**必要定义**，代入 (1)，并用完整原 NS/PS 直接检查同点原迹。它们对 $\alpha$ 至多二次，不用旧九条正乘子二次化。

令五个实际原二次为 $P_i$，其中前三个是 $Q_j$。对每一行仅减
$$
L_i=P_i-[\alpha^2]P_i\,q_\alpha
=r_{i0}(\chi)+r_{i1}(\chi)\alpha.
\tag{3}
$$
完整返回 (3)。其真实 $\alpha$ 倍在首一环境中为
$$
\alpha L_i\equiv-r_{i1}q_0+
 (r_{i0}-r_{i1}q_1)\alpha\pmod {q_\alpha},
\tag{4}
$$
并实际核回完整商项 $r_{i1}q_\alpha$。

因 (2) 本来属于前三原式理想，(3) 双向保原五式；native 两原三次的系数一又保证完整 $I_6$。所以这十个真实两列行是原 $I_6$ 在自由秩二环境
$$
A_W[\chi][\alpha]/(q_\alpha)
$$
中的**完整理想像**，不是仅必要矩阵。列方向始终是 $(1,\alpha)$，没有假定最后商自由，也没有假定任意两列操作代表原乘法。

每行只清已付权分母、剥已付纯权内容。所有未付的 $\chi$ 内容均保留。源逐行输出准确 checkpoint，不为大来源展开额外重复运算。进一步定位物理 $t,D$ 等须按原图进行，不称定位后仍对 $A_W[\chi]$ 有限自由。

## 5. 三个固定新原标量

十行顺序为
$$
L_0,\alpha L_0,\ L_1,\alpha L_1,\ L_2,\alpha L_2,\
L_{NS},\alpha L_{NS},\ L_{PS},\alpha L_{PS}.
$$
只取固定两行组 $(6,8),(6,7),(0,6)$。对两行后列取实际消元乘子 $(b_1,-a_1)$，只除这两个真实乘子的完整共同因子，随后重新核验两列为 $(C,0)$ 和完整 $\alpha$ 多项式身份。

这保留该共同因子的整个零集，不把某条原方程除以未付因子。最终目标只剥当前原权单位；新的 $\chi$ 头、权内容、所有参数零面全保。若目标或乘子为零则照零记录；非零非单位只给原必要约束，不以多元 gcd 判空。

## 6. 唯一源与资源

basename：2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py。

源码 14136 字节，SHA256 18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b。

唯一固定依赖：
2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py，
完整 SHA256 10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1；
只取 matrices/errors 定义前 14656 字节，
前缀 SHA256 88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8。

180 秒/4 GiB。所有嵌套 alarm/setitimer 钳制到顶层同一绝对截止；没有旧低硬限后冒称更高值。只保存源、参数定义、次数/SHA、小回执，不输出或存储可重算的完整系数、矩阵或证书数据。实际退界只登记已完成 checkpoint，不补猜后续原返回。
