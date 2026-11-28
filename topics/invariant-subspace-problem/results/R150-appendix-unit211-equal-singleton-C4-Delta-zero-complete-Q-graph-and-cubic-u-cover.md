# R150：碰撞C4、Delta零的完整Q图和三次u覆盖；有理cofactor超时冻结

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

**已完成部分。** 在整个
$$C_4(\lambda)=\lambda^4-3\lambda^3+3\lambda^2-\tfrac32\lambda+\tfrac38=0$$
常数代数上，h=k、Delta=0的原Q首项零面已准确排除，Q在所有原点都由同一个有理u式恢复。原Tnum再给一个完整首一三次u式。因此不同(lambda,u,Q)原基点至多12，全部常数嵌入保留。

**2026-11-28 原来源更正：** 本页 Q 图及原 Tnum 三次独立保留；旧紧凑 R 使用了错误平方系数，因此“四个紧凑原行”的整体原必要性撤回。首个有理 cofactor 未返回并继续冻结。后继独立真 Gram 已闭合附加 C4 条件；正确全支范围见[三个小因子及4788界](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)。

## 1. 原Delta的整个线性Q图

令K=QQ[lambda]/C4。沿用原碰撞值常数
$$A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,$$
$$\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B.$$
在整个K中准确有ell=1、T=xi。仍取
$$S=2\xi+3-2\lambda,\quad\eta=\xi+3-2\lambda.$$
令
$$c=3-4\lambda+\xi\eta,$$
$$H(u)=(c+S\xi)u-2c,\quad
C(u)=2\xi u(u-1)(\xi u+2\eta).$$
原Delta完整展开为
$$\Delta=-2(u-1)\{H(u)Q+C(u)\}.$$
由于u-1已支付，所有原Delta零点都必须满足H Q+C=0。

新源在完整K[u]上实际得到
$$\gcd(H,C)=1,$$
并乘回其完整Bézout。没有使用u参数逆。因此H=0与原Delta=0不相容，整个Q首项零纤维已排除，而不是保留一个未检查例外后只处理一般点。可以准确恢复
$$Q=-C(u)/H(u). \tag{1}$$

实际完整Q图在0.111秒前返回。原Delta在同一(1)上恒为零，后续所有原式使用这个Q，未混配根。

## 2. 同点原Tnum的完整三次u覆盖

在(1)上从原定义构造Pf、Pc、NF、NC及
$$T_{\rm num}=P_fN_C-P_cN_F.$$
实际分子只剥原单位因子，全部除法与总乘积返回。真实记录为u因子三次、u-1因子三次，以及原Q分子的一个一次gcd因子。最后一个记录不表示整个Q多项式的一次幂。

首一残式为
$$g(u)=u^3+g_2(\lambda)u^2+g_1(\lambda)u+g_0(\lambda). \tag{2}$$
下面每行按lambda的升幂给出全部系数：

| 系数 | 常数项 | lambda项 | lambda²项 | lambda³项 |
|---|---:|---:|---:|---:|
| g0 | -1935968/377807 | -582832/377807 | 2333440/377807 | -734336/377807 |
| g1 | 86116/10211 | 82696/10211 | -151584/10211 | 33024/10211 |
| g2 | -1726012/377807 | -2265096/377807 | 2999120/377807 | -176192/377807 |

(2)在62.419秒前完整返回，包含所有u根。对每个C4复嵌入至多有三个不同u值，且(1)唯一恢复Q，故至多12个不同基点。没有宣称三次式在K中不可约，也没有忽略可能的分裂或重根。

## 3. 错误紧凑 R 的隔离与冻结后段

旧源确实构造了四个紧凑 z 二次，但其中 R 的平方项来自已撤回的错误 compact 定义。因此该四行整体不能作为原必要条件，不恢复原来源声明。

保留的准确身份是
$$
P_fNV=T_{\rm num}-bc\Delta z.
$$
完整静读确认 Delta、Tnum 在错误紧凑行之前按独立原定义给定；后续 g3 只从该 Tnum 的分子剥已付支持，没有读取错误 R。故第1、2节的全 Q 图和三次仍是原必要条件。

四紧凑行的历史完成时间为62.384秒；它仅记录当时执行发生，不构成新的原证明。后续首个有理 cofactor 未返回任何完整三列身份，120秒 SIGALRM 仍保持冻结。独立十二维真 Gram 返回不依赖此错误行或未成 cofactor。

## 4. 完整实际执行身份与转向

源：
[2026-11-27-unit211-equal-singleton-complete-C4-Delta-zero-Q-graph-original-means-8542.py](../notes/2026-11-27-unit211-equal-singleton-complete-C4-Delta-zero-Q-graph-original-means-8542.py)。

源blob f2d555ac62e231023c27962e75f82533a7020498，SHA256：
5b2b2fcd2706e2bbe6761b38055cd42ac6ccd63e944f8e4f8a7fd5cf5503d0aa。

实际run46032150195/job140618367875；120.070572019秒，最大子进程RSS41680KiB，内层exit -14（SIGALRM）。stdout2218字节，SHA256：
0651e6df6cda513ce7c37cc4dcdba366a48f3ba20335635836d7dde939610521。

真实pull在2026-11-27 16:16:23.720245 UTC读到c03e68ac712e5aff12a42667d5316537cb46cc79，两README未变。已完成的每项数学返回按上述准确时间保留，失败范围只在尚未完成的后段。

新输入直接使用(2)的全部系数，在K[u]/g中恢复同一个lambda、u、Q，再返回原八Gram条件和整个自由f。遇到任何非单位逆时须准确分成两个u因子并继续两支，不能丢掉分量。不重跑本次有理u cofactor，也不提高其时限。整个碰撞Delta零及普通Hilbert ISP仍未完成。
