plugins {
	`kotlin-dsl`
}

group = "com.qiusuo"
version = "0.0.1-SNAPSHOT"
java.sourceCompatibility = JavaVersion.VERSION_11

repositories {
	mavenCentral()
	maven { url = uri("https://repo.spring.io/milestone") }
}

dependencies {
	implementation("org.jetbrains.kotlin:kotlin-reflect")
	implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
	implementation("org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.31")
    implementation("io.spring.dependency-management:io.spring.dependency-management.gradle.plugin:1.0.10.RELEASE")
}