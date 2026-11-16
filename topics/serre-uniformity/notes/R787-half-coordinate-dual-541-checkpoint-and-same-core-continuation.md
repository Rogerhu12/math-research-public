# R787 半坐标 dual 的真实541位断点与同核续接

日期：2026-11-16。会话：serre-public-astra-20261115。**A.1仍未决定；这是实际断点与续算记录，不是数学接受或拒绝。**

原半坐标run [43823979328](https://github.com/Rogerhu12/math-research-public/actions/runs/43823979328)，compute job133153392094，source6110d6a16d2e66becae71454ad2d4e796b7a5c00，于2026-11-16T12:31:44.927947+00:00按核心预算结束。实际退出码124，core receipt存在，核心用时18011.659813753秒；不是外层失联或伪造结束。

## 1. 实际已成与未成

原完整dual的370位被准确导入，此新链提交171个新位，最新完整精度为541。172条历史记录包括原370位起点；最新两条540/541都保完整原模恒等式与半坐标必要条件，并逐SHA接前一current。

最新current为40953867B/e7b19461，完整535至541等既成位不重算。542位的原正残差也已原子完成（141153B/59b1a8d7），而其修正尚未完成；新请求从该现成残差接续，不重求它。最后一个真实RR尝试在536位，失败不构成q的拒证。

原候选值严格拒绝、A.1行空间为零、准确dual有理解、原y/x/导数的准确展开以及eta/height，当前终点均明确false。完整准确出口继续保[HP三种终点](R787-half-coordinate-dual-continuation-source-contract.md)，七支解/半坐标不能替代原35840个有理坐标的最终验证。

## 2. 同一核心与原输入

数学核心ffe5dcff0c17b81923741c2b56806cc4907cb812cfdee4499ed2650ea92abe54、wrapper1552e403d9206d21a7cd7de43c1e7f4975957513e332a316c448fccbb84c46f4保持不变；实际数学configuration指纹为368848b4dff60395891899f21eea3ff22f9ced1b1715c66c5e3cef50ed4d95a5。

原completed_dual_source仍绑定370位父源，不能把它改填541而使数学tag换源。本次只把resume绑定刚结束的半坐标run；恢复现有同tag全部完整阶段、541 current、542正残差和原历史，下一新算术是542修正及完整乘回。

原输入仍为CM87、R781134、R7864、R7871256，共1481件。原331720235B输入包fe7c4126、配对包247572B/08ea733d及旧完整dual包31300663B/6c476884都由当前一日artifact直接带入，不依赖已过期的祖先重取，不重旧逆/目标/配对/CM或Laurent。

运行预算300分钟，最大新位数null，每8位原严格RR；这些运行控制不改变数学身份。未得完整终点就继续从实际新断点接续，预算退出不算负结论。

## 3. 实际文件身份

|文件|字节|SHA-256|
|---|---:|---|
|full-outputs-manifest.json|6025|b274f3b40e8c98f265ebf458fb2cd92ae0daa3828c5714da0386328f091ca129|
|R787-cleared-dual-current-00000541.json.gz|40953867|e7b194614b11a85166e04fb2cfba8c3676d0197896436d73719ed7d492b653fa|
|R787-cleared-dual-current-index.json.gz|5983|5d0e369244aea3100aca1286d39ffd45461cf665e0c9b4e88eefaabe165a3f72|
|R787-cleared-dual-step-00000542-positive-residual.json.gz|141153|59b1a8d7eec5636aad786bfac30ecc97f98f718cd57596798b1697909019f133|
|R787-cleared-dual-checkpoint-history.json.gz|35923|1b905ec86ae36ee6736df088bbb4281d2df8b4e99186df929d3cb4de7d402c58|
|R787-cleared-dual-exact-target.json.gz|2743532|276ec03e58a99db7da9243ac6b074a29818a17cb0233789403b6fecd78061b1f|
|R787-cleared-dual-half-source-audit.json.gz|13417|0de83a584b72a99abeb710b5441ed0ab64cd8003d549b7c644dda21e3bd031c3|
|R787-cleared-dual-stage-manifest-a001c13b9a838af8e188d5ce.json.gz|7471|839b2a29117c11e42240a02e083308e2cc8713d669fa449d6866e0db7052125b|
|p41-original-cleared-dual-CM-value-acceptance-certificate.json|14342|55cb278b7a19d354a69c256cb196bb4791004faefb9884af1870e63b077b4722|
|core-receipt.json|12989|326276277814652e6fe7f59d645915fd009ca3cc107af967aadc966fcfbdc364|
|public-actions-input.json|283047|a3b867bb59c607f8e924514ffc8a9e689755afe76345536e692afd9f24425c48|

完整manifest共39项。原一日artifact14226237212，名称serre-global-R787-half-coordinate-dual-CM-value-43823979328-1，ZIP408220668B/263ebd784207dae07506abbba30988768a98620d4bc324ed7b4e3f4228f53719，到期2026-11-17T12:31:47Z。

必要纯IO run43868454199/job133303099690/source d3f71b7dbdcfd014f4130779d7f2a6a78b252b2a，13次Range实读991600B、12件小源。根读完整manifest、终点、core与run receipt、index、历史及原输入身份；没有宣称重哈希原408MB ZIP或40MB current。

小转入包339612B/83470d583453ba5e4cfd1098c320f51f3ad6647caaf638833ae2a3978373946c；其一日artifact14225684352、365881B/aaa53680e80889c5d1e8f7d515d4a5a9305cfb0a6f82575b84d736cde8c130a1实际整包SHA已核。该包仅用于必要读取，续算直接消费原完整artifact并逐原SHA恢复真实live阶段。

所有新数学仍仅在本公开仓库Actions，原raw、矩阵、current和回执不写入Git或Release。主Serre一致性目标继续OPEN。
