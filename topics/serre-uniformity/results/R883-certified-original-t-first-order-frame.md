# R883：原 t 参数的实际首项单位与标架方向已认证

## 1. 实际结论与准确范围

公开 [run 43843430426](https://github.com/Rogerhu12/math-research-public/actions/runs/43843430426)，
compute job `133217615987`，source
`a41eaf283496222761525ba06efd1e3d61ab4f47` 已实际 success。
核心在 **0.186012313 秒**内完成五个数学阶段，直接复用 28 个所需原成员；
旧 Hensel jets、原固定逆、Fourier 长尾及原坐标基没有重算。

在原 $P_0$、原 $\rho=z-z_0$ 和指定辅助素点
$\mathfrak q\mid1000000753$，本次已认证原标记参数
\[
 t=a^3=\frac12+\frac{E_6}{48s\eta^{12}}
      =c\rho+O(\rho^2),\qquad s^2=-3
\]
满足
\[
 c=\frac{a_1b_0-a_0b_1}{48s\,b_0^2},
 \qquad c\bmod\mathfrak q=354813668\ne0.
 \tag{883R.1}
\]
这里 $a_i,b_i$ 是下文两个原截面的准确 jet 系数。
该式给出原 $K=\mathbb Q(s)$ 中的准确来源表达式及其合法约化，
不是将一个有限域数冒称为已展开的特征零常数。

本次的单位断言是**指定辅助素点 $\mathfrak q$ 的单位**，
不由此断言 $41$ 处、所有非 $p$ 处或某个整模型的单位。
原 $t(P_0)=0$ 的特征零事实来自既成 R802/R872；
非零一次项证明此原 $t$ 在 $P_0$ 确为局部参数。

## 2. 原截面、共同尺度及准确相消

原 R807 的两条截面由本次来源审计按其原 producer 身份读取。
[执行方法](../notes/R883-original-t-first-order-frame-method.md)
与请求中钉住的原文件/bytes/SHA 给出准确入口。
原截面本身严格为
\[
 N_{692}=\theta(82^6E_6),\qquad
 N_{693}=\theta(82^6\eta^{12}).
\]
原 $\theta$ 使用 $82^2$ 的 M2 尺度，原 V4 基使用 $82^8$ 尺度。
令
\[
 A(\rho)=N_{692}/\tau^4,\qquad B(\rho)=N_{693}/\tau^4.
\]
则准确函数域恒等式为
\[
 t=\frac12+\frac{A(\rho)}{48sB(\rho)}.
 \tag{883R.2}
\]
原 $\theta$、$82^6$ 和同一 $\tau^4$ 各相消一次；
没有再插入 $82$，没有改变 $s$ 的嵌入，也没有换另一条有相同零点的参数。

原 $\theta$ 的准确消失阶至少二已有原 E6 主部证明。
本次实际评价其前三项，并认证第二项约化非零，因而其准确阶恰二。
前两项的模零仅核其约化，与准确消失的既成证明分别保留。

## 3. 直接复用原 jets 与 recipe

原 R872 矩阵有 273 行、418 列，列为
$z^k\beta_i$，正常次数
$\epsilon=(0,1^{144},2^{127})$。
本次只选其阶 $0,1,2$ 的既成行及相应原列。

原 R805 的 $n=1$ 给原 146 个一次函数
\[
 e_0/\tau=1,\qquad e_1/\tau=z-\beta_{72},\qquad
 e_i/\tau=\beta_{i-1}\quad(2\le i\le145).
\]
沿原 R801 recipe，逐叶组成原 962 个 V4 单项式的三个系数。
每个节点保原 reference index、四个叶因子、整数尺度及完整指纹。
来源审计实际核对：

- R807 与 R801 的原 R775/R786 身份相同；
- R807 与 R872 的原 R805 身份相同；
- 原 $P_0$、$\rho=z-z_0$、$\zeta=549966761$、$s=99932770$ 一致；
- 两截面各自的准确有理坐标分母均在 $\mathfrak q$ 为单位。

因此只进行了新的长度三截断乘法和原坐标求值。
两个坐标向量的各自共同分母均只除一次；
没有从近似数值重新识别基，也没有重新解旧 Hensel 系统。

## 4. 实际单位与完整三系数乘回

本次实际取得
\[
 b_0=B(0)\bmod\mathfrak q=829783888,
 \qquad b_0^{-1}\bmod\mathfrak q=91131767.
 \tag{883R.3}
\]
故准确 $B(0)$ 在指定辅助素点为单位，式 (883R.2)
可在原 $P_0$ 局部环直接展开。
程序没有删去一个仅在模素数下为零的初始段。

写 $A=a_0+a_1\rho+a_2\rho^2+O(\rho^3)$、
$B=b_0+b_1\rho+b_2\rho^2+O(\rho^3)$。
三项除法之后，程序完整乘回 $B(A/B)=A\bmod\rho^3$，
并得到原 $t$ 的实际约化
\[
 t\equiv354813668\,\rho+69017137\,\rho^2
       \pmod{(\mathfrak q,\rho^3)}.
 \tag{883R.4}
\]
一次项与式 (883R.1) 的导数表达式完全一致。
所有分母的单位性及该非零约化证明准确 $c$ 为
$\mathcal O_{K,\mathfrak q}$ 的单位。
这没有把仅有约化信息的二次项称为其完整特征零展开。

准确来源 DAG 同时保留原 Hensel 关系
\[
 \ell(x)W(z(x))=w(x)\ell(x),\qquad \ell_0(x)=1,
\]
原 R856 常数点及原 R868 单位子式。
原规范化和 Hensel 唯一性固定的正是原 $P_0$ 分支。

## 5. 标架方向与实际幂

若原函数在 $\rho$ 中有首项 $L\rho^{-m}$，
由 $t=c\rho+O(\rho^2)$ 直接得到
\[
 L\rho^{-m}=(Lc^m)t^{-m}(1+O(t)).
 \tag{883R.5}
\]
因此原参数转换是**正乘 $c^m$**。

| 后继使用 | 准确帧表达式 | 本次对应的 $c$ 幂约化 |
|---|---|---:|
| R879 原参考单极函数 | $c^{254}/U_{272}$ | $c^{254}=485783778$ |
| R887 翻转后原主函数 | $L_f\ell_Cc^{1205}$ | $c^{1205}=201313487$ |
| R880 翻转前原主函数 | $L_fc^{1457}$ | $c^{1457}=902983214$ |

表中等号数值均只指模 $\mathfrak q$。
$U_{272}$、$L_f$ 与 $\ell_C$ 仍引用各自原消费者，
本次没有重新计算或把它们归一化为一。
原 R879 参考铅笔与 R880/R887 主因子方向保持不变。

## 6. 完整输出身份

核心与同任务标准库 IO 读回均实际 success；
IO 没有执行新的数学。实际 configuration SHA256 为
`ea27184f1beb64978adfa1940cf0b01343461e978319b4531b283d5b80b62a99`。

| 文件 | bytes | SHA256 |
|---|---:|---|
| `p41-original-t-first-order-frame-certificate.json` | 9033 | `3ae22a7651cecd492c170c44a034bea71356e01bd4fdc880851b86742298daeb` |
| `R883-original-source-audit.json.gz` | 3444 | `e1ef1791ab44ca3f875713d10c2184befd99a858f7e5aefceddbea6e47d57043` |
| `R883-original-M2-three-jet-leaves.json.gz` | 6150 | `c9282958d1e39a4fc3be498caf7ef3dede8ee90f62231eb553d86862cb3f19c5` |
| `R883-original-V4-recipe-bridge.json.gz` | 97106 | `b384db529231c762cd73f3390d6841a8361ef1e9f83800cba05bc1e6f37758ff` |
| `R883-original-cleared-section-three-jets.json.gz` | 3813 | `a6e82398385d7ea391100238905e80736aeddb5797ddb84033c0d8f394c42573` |
| `R883-original-t-first-order-unit-and-frame-DAG.json.gz` | 3850 | `136dd22c3aaddb0b650a5513eefd6db70bfee8a088f0f0cd437a5b6927f6094a` |
| `R883-original-source-inventory.json` | 6861 | `25529c0eef9da00ac7872d13f6c358fa0da9114f77735363979258d340e5a3fc` |
| `full-outputs-manifest.json` | 2783 | `d2e9de1f1d969695f1d7b8b3ebbd933264d292e377113f622ed623a68076390f` |

原数学 artifact `14214835037`：
`serre-global-R883-original-t-first-order-frame-43843430426-1`，
8018550 bytes，平台 ZIP SHA256
`3041116aa53b458e37635b8b5fccab6a2b988f4a57a05d6e5ba086229f0392bc`，
到期 `2026-11-17T09:51:15Z`。
保留的原小来源已在本次必要 artifact 中续存；
继续消费不依赖重新运行原 R807/R801/R872 producer。

核心 SHA256
`2778a81b5639a1eb6285718574af0ce4b48b00e92b648c6ac29ffe70c1da66f7`；
wrapper
`91799e07dbf3a5875734df8fb4fdb3e4e15e7427195647973e76ac3ce82da76b`；
执行方法
`a3775894517263ec34dd4b949e985b7db3536e81cec10cb8d9f5d7f8b2b4e8b1`；
实际请求
`9927874c31f7b76b3aa5d48f0bb99a8028e76d4a0d4c1164abda8bab838e7079`。
所有完整原机器输出仅保必要的一日 artifact，未进入 Git 或 Release。

## 7. 已关闭与继续工作

本结果关闭原 $t/\rho$ 首项的准确来源与实际辅助素点单位校准，
并确定三个现有框架的转换方向和所需幂。
五个原 $L_j$ 的 128/144 空间、整个 Picard 刚性化、
连接、Poincaré period、theta 二挠、非 $p$ 项及原高度仍未完成。
这些字段在实际证书中分别保持 false。
