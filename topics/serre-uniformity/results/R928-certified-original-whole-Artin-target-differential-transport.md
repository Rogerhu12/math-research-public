# R928：原完整 Artin 对应的目标微分输运实际认证

日期：2026-11-16。本篇登记已经完成的公开计算：八个原分子系数导数、目标第二坐标的完整商法则、全部目标正常坐标上的 $g_t,h_t$，以及整个秩八对应上的微分输运系数 $J$ 已认证。七连接求值、Gal7/cY 数值作用及高度仍未完成。

## 1. 实际运行与准确来源

本次 [run 43918212179](https://github.com/Rogerhu12/math-research-public/actions/runs/43918212179) 的数学 job 为133478138738，source 为10288e01680361bddf2a650cd98c38eb7b47889e，实际 success/exit0。core 时长1.514405222999983秒，57个完整 stage，另一个 current；这些都是实际 receipt 与 complete IO 给出的计数。

|冻结执行件|SHA256|
|---|---|
|core|f899af1a65b2243c47a738bedc6eff3954502b4e3867ab59ae56d80cca045337|
|whole Artin helper|e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d|
|wrapper|83d6c51ac1b34e432ac768341363eb090ea7cb24829c03236d05ff7d1abf4fd7|
|method|1a0a9cf2b4ffd5d9edc20cb17e6eea59959d2fcbe4785b76621b6581687ceaa4|
|active request|a3b3492c581f80c43451282a6a26b64097076a7f88820d974ab370999581d992|
|workflow|26bb2e7edbd9fed04a1e6a1c5daf2929a52ae5a07e98d545053c4515aeca2585|

实际数学 configuration 为68132fe8e1e35804bde764cee49cba9d4f207630963303b8c44033dbf0693f5d。规则 job133478064436 在2026-11-16T17:25:33.967487+00:00 真正 pull main 至10288e01680361bddf2a650cd98c38eb7b47889e，根与课题 README 的 SHA 分别为6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9、35f82f3d96f1e07d1b7c3f0320398fdc0cd68d0c0e55ac17881c9f976299646d，均无变化。

数学依据是 [R922 完整目标求值公式](R922-original-bounded-connection-numerators-and-whole-Hecke-evaluation.md)，其全文 SHA 为75e0e04e986203598b556403b4ea8eec3706da838e934ae11810c5abda569731。实际方法见 [R928 method](../notes/R928-original-whole-Artin-target-differential-transport-method.md)。

直接消费93个旧原文件：R919的47件、R885的27件、R827的6件、R882的7件与R873的6件。R919旧载体中的73个原成员先按其原 inventory 读过并保持身份，再保留当前所需的46件旧四组来源；它们不改标为新数学 stage。R827 原历史 exit124、result 位于 configuration 及无成功 FINAL 的例外按原来源处理，未伪造成功。

## 2. 原对象和微分方向

源仍是同一个原辅助处 $\ell=1000000753$、源 $z=0$ 的完整272维代数 $A_0$。目标为原完整秩八代数

$$
E=A_0[U]/(P(U)),\qquad \dim_{\mathbf F_\ell}E=2176,
\tag{928.1}
$$

其中首一表示、原领先系数 $a_8$、原 $P_U$ 及两者已成单位逆均逐字消费。原第二目标坐标是

$$
V=K(U)/P_U(U).
\tag{928.2}
$$

R873/R882 的后八列是分子 $K$ 的系数；没有把它们当成 $V$ 的系数。$\delta=\nu^{-1}d$ 始终先在原函数上作用，再取指定纤维；不声称 $\delta$ 降为商代数 $A_0$ 上的导子。

[R919 已成结果](R919-certified-original-whole-Artin-Hecke-differential-trace.md) 的九个 $\delta P$、$\dot U=-\delta P(U)/P_U(U)$、33个原正常基导数块、旧 $P_U^{-1}$ 和全部272目标正常坐标均直接复用，不重算旧 $\Gamma$、逆或九列导数。

## 3. 八个新 delta K 与完整商法则

使用原R882同处的17列系数，新增的仅为最后八列与原正常函数导数的收缩。33个已成导数块逐块给八个 $\delta K_i$，其余九列不再计算。对真实目标 $U,V$ 定义

$$
\Delta K=(\delta K)(U)-V(\delta P_U)(U),\qquad
H_K=K_U(U)-V P_{UU}(U).
\tag{928.3}
$$

然后只用旧已成逆形成

$$
\boxed{\quad
\dot V=P_U(U)^{-1}\bigl(\Delta K+H_K\dot U\bigr).
\quad}
\tag{928.4}
$$

这是在原关系 $P_U(U)V=K(U)$ 上求导所得，保留系数微分及变量微分的全部项。实际输出保存 $\delta K(U),K_U(U),\delta P_U(U),P_{UU}(U),\Delta K,H_K,\dot V$，以及 (928.4) 清分母后的完整左右向量；全部2176个坐标相等。

这里的 $P_U^{-1}$ 来自原R885真单位证书，不以有限点值替代，也不删除分歧或幂零部分。

## 4. 真目标 g、h 及一个完整单位框架

原 $g,h$ 的正常坐标为四个 $z$ 系数向量。先与已经完成的全部272个目标正常函数 $\beta_i(U,V)$ 收缩，再对 $U$ 做 Horner 求值。17个原目标块完整参与，得到

$$
g_t=g(U,V),\qquad h_t=h(U,V)\quad\text{于整个 }E.
\tag{928.5}
$$

这一步不使用源 $z=0$ 的 $g,h$ 数值代替目标函数。

按原整数顺序试 $\ell_t=g_t+t h_t$，实际已取得一个在整个 $E$ 中可逆的值及其完整证书。单位证明保留秩八 Berkowitz/完整 Cayley–Hamilton、源272维未约化多项式上的 Bezout 证书及最终2176坐标逆乘回；不先选几何点或删除坏因子。本篇不从摘要预填实际选中的整数，它保存在完成 stage 中供后继直接消费。

由该真单位定义

$$
J=\ell_t^{-1}(\dot U+t\dot V).
\tag{928.6}
$$

实际同时核全部2176坐标的两个恒等式

$$
\boxed{\quad Jg_t=\dot U,\qquad Jh_t=\dot V.\quad}
\tag{928.7}
$$

因 $g_t,h_t$ 共同给原目标微分框架，(928.7) 明确识别了 $\nu_t=J\nu_s$ 的系数。**没有求 $J^{-1}$，也没有把 $J$ 本身为单位加入接受条件。** 原对应可能出现的微分退化不能被这一不必要条件排除。

## 5. 真实完成文件

|实际成员|字节|SHA256|
|---|---:|---|
|p41-original-whole-Artin-target-differential-transport-certificate.json|20552|713fcc41b6276513dbad0110fa660963d9d8c93c91f95007c29ab8bb69e66f5c|
|full-outputs-manifest.json|9882|6095a0628dd530ddd6a6008bffa0976e88451e722c4242710134d4e3ce92cfa6|
|R928-eight-original-delta-K-coefficients.json.gz|21136|920bfe12881da4197c4b9e0289e59dbed05b192c2341b6964f5f0bee5f356c78|
|R928-whole-quotient-derivative.json.gz|96268|2d15be76c7a88848295b3a068fe3c521015b9bcfbcdd2207139deb5bb44e26a3|
|R928-whole-target-g-h.json.gz|31779|1f5b6bd905b3b031c3cff9bd51ea607cfb3d9bc3b630579b657dec68125329f0|
|R928-complete-target-differential-transport.json.gz|41536|cea050abb47f452df115d366b3634c5e27f7371e32bfa01f63e0907bad19c042|
|R928-original-characteristic-zero-target-transport-DAG.json.gz|8846|cc5e9c2e58e44927bd57aac387ca9ec572426a38c2f3ecde5ca582df551f4b9b|
|R928-retained-original-inputs.tar.gz|15081891|effd19da84b57607c8e32e9aec7c2773a84168e0606a6cabf904262cc2766dd1|
|R928-original-source-inventory.json|38994|2146a42f79c691a3539e049933110828a6f4cb9acacd0324512497996f5a6be9|

实际一日 artifact 名为serre-global-R928-whole-Artin-target-differential-transport-43918212179-1，ID14250307542，17419419字节，平台 archive digest 为6535112c49a5f1fdd582abbf7ad4589f17e7ad95fefee2fb0e3b976beb5b136e，到期2026-11-17T17:26:00Z。上述逐成员 SHA 是实际完成 IO 输出；平台整个 ZIP digest 未被冒称为外部重新哈希。

## 6. 准确表达式与未完成边界

准确特征零 DAG 保留原 $P,K,V$、系数微分、商法则、目标正常函数和单位框架定义。有限域数组是该指定原地方的实际值；未展开新的全部特征零导数系数，也不将源纤维上的数值改写成全局函数恒等式。

直接方向仍为原 $\pi_s,\pi_t$；canonical dual7 同构同时运输两个 determinant frame。scalar7、diamond、原 $-3$ 下降、$\kappa,\nu$、端点与极化标记原样保留，本次未重新求其数值标定。

后继R930可消费 [R922 的低权 $R$](R922-certified-original-shared-polynomial-trace-dual-multiplier.md)、[R926 的七原 $d_D,y_D$](R926-certified-original-seven-bounded-connection-polynomial-numerators.md) 和本篇 $J$。但它仍须真实验证每个 $d_D(U)$ 在整个 $E$ 为单位，再评价并取完整秩八乘法迹。五个 Picard 组合所需的原 $\sigma,c_Y$ 及主函数叶不能由七个基连接的来源定义自动冒认已计算。非 $p$ 项、Poincaré period、splitting、height 和绝对一致性主目标仍 OPEN。
