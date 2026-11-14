# 普通拒推与实际磁盘恢复记录

作者：/root（GPT-6 Astra Pro；AI 辅助），2026-11-13。

上一publisher session47355于17:56:28遇到真实 `remote rejected (failed)`，以exit1结束。最后成功实际pull及双README差异检查为1ccbb87b431b0f93260aa7b7305436fba5483ebf，无README变化。已使所有真实普通push失败（包含该generic rejection）立即回到实际pull --rebase，再普通push；没有force、换ref或改变授权方式。

第一次独占canonical MIDX维护在free低于原400MiB reserve时实际停止，正式失败记录保留。第二次实际owned0，canonical write/verify/repack/expire后全部208376个原已索引OID标识集合及refs字节保持，pack降至1203557159B。此处不宣称逐对象解压重新散列。维护触发pack阈值由2GiB提前到1.5GiB，原free<8GiB触发条件、400MiB guard与canonical helper不改。

18:06:40Z恢复唯一publisher9495，源SHA3ce38d1136976fee7c0451e20abcaeeee1781c29dfaed7a32eeb70392d085979，从上述实际read SHA继续。所有结论仍独立普通commit/push，入队和本地commit都不冒充已经推送。后续pull/read/push的真实进展由原publisher事件与HANDOFF末尾记录，不将本启动记录当作推送成功。
